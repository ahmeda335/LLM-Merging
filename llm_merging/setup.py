"""Install the llm_merging library"""


from setuptools import setup

setup(
    name="llm_merging",
    version=1.0,
    description="starter code for llm_merging",
    install_requires=[
        "torch", "ipdb"
    ],
    packages=["llm_merging"],
    entry_points={
        "llm_merging.merging.Merges": [
            "llama_avg = llm_merging.merging.LlamaAvg:LlamaAvg",
            "flan_t5_avg = llm_merging.merging.FlanT5Avg:FlanT5Avg",
            "our_method_llama = llm_merging.merging.OurMethodLlamaAvg:OurMethodLlamaAvg",
            "our_method_flanT5 = llm_merging.merging.OurMethodFlanT5Avg:OurMethodFlanT5Avg"
        ]
    },
)