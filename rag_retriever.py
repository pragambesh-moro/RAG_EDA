################################################################################
# Copyright (c) 2026, Shiv Nadar University, Delhi NCR, India. All Rights
# Reserved. Permission to use, copy, modify and distribute this software for
# educational, research, and not-for-profit purposes, without fee and without a
# signed license agreement, is hereby granted, provided that this paragraph and
# the following two paragraphs appear in all copies, modifications, and
# distributions.
#
# IN NO EVENT SHALL SHIV NADAR UNIVERSITY BE LIABLE TO ANY PARTY FOR DIRECT,
# INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST
# PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE.
#
# SHIV NADAR UNIVERSITY SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS PROVIDED "AS IS". SHIV
# NADAR UNIVERSITY HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,
# ENHANCEMENTS, OR MODIFICATIONS.
#
# Revision History:
# Date          By                     Change Notes
# ------------ ---------------------- ------------------------------------------ 
#               Pragambesh Moro        Initial commit
################################################################################
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class CadRagRetriever:
    def __init__(self, db_dir: str = "./chroma_db"):
        print("Loading BAAI/bge-small-en-v1.5 Embeddings...")
        # Re-initialize the same embedding model
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        
        self.embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        
        print(f"Connecting to Local ChromaDB at {db_dir}...")
        self.vectorstore = Chroma(
            persist_directory=db_dir,
            embedding_function=self.embeddings,
            collection_name="cad_commands"
        )
        
    def retrieve_context(self, query: str, top_k: int = 3) -> str:
        """
        Takes a plain-English query, searches the Vector DB, and 
        returns the top_k most relevant markdown chunks formatted as context.
        """
        # BAAI/bge-small models require this specific prefix to enable asymmetric semantic retrieval
        bge_query = f"Represent this sentence for searching relevant passages: {query}"
        
        # Perform Cosine Similarity search
        results = self.vectorstore.similarity_search(bge_query, k=top_k)
        
        context_blocks = []
        for i, doc in enumerate(results, 1):
            source = doc.metadata.get("Source", "Unknown Manual")
            header1 = doc.metadata.get("Header 1", "")
            header2 = doc.metadata.get("Header 2", "")
            
            # Format the context block nicely for the LLM
            block = f"--- CONTEXT BLOCK {i} ---\n"
            block += f"Source: {source}\n"
            if header1 or header2:
                block += f"Hierarchy: {header1} > {header2}\n"
            block += f"Content:\n{doc.page_content}\n"
            context_blocks.append(block)
            
        return "\n".join(context_blocks)

    def retrieve_random_context(self, k: int = 3) -> str:
        """
        Retrieves random context chunks by searching for a random string,
        simulating 'Wrong Retrieval'.
        """
        import random
        random_query = f"random meaningless query {random.randint(1, 1000000)}"
        results = self.vectorstore.similarity_search(random_query, k=k)
        
        context_blocks = []
        for i, doc in enumerate(results, 1):
            source = doc.metadata.get("Source", "Unknown Manual")
            block = f"--- CONTEXT BLOCK {i} ---\nSource: {source}\nContent:\n{doc.page_content}\n"
            context_blocks.append(block)
            
        return "\n".join(context_blocks)

    def retrieve_partial_context(self, query: str, k: int = 3) -> str:
        """
        Retrieves relevant context but truncates the content to simulate 'Partial Retrieval'.
        """
        bge_query = f"Represent this sentence for searching relevant passages: {query}"
        results = self.vectorstore.similarity_search(bge_query, k=k)
        
        context_blocks = []
        for i, doc in enumerate(results, 1):
            source = doc.metadata.get("Source", "Unknown Manual")
            # Truncate content to first 50 characters to make it "partial"
            truncated_content = doc.page_content[:50] + "... [TRUNCATED]"
            block = f"--- CONTEXT BLOCK {i} ---\nSource: {source}\nContent:\n{truncated_content}\n"
            context_blocks.append(block)
            
        return "\n".join(context_blocks)

if __name__ == "__main__":
    retriever = CadRagRetriever()
    
    print("\n" + "="*50)
    print("TESTING RETRIEVAL PIPELINE")
    print("="*50)
    
    test_query = "How do I create a floorplan with 0.7 core utilization?"
    print(f"\nQUERY: '{test_query}'\n")
    
    retrieved_context = retriever.retrieve_context(test_query, top_k=3)
    
    print("RETRIEVED CONTEXT (This is what the LLM will see):\n")
    print(retrieved_context)
