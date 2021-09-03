# PoetryTranslationEMNLP2021

Training and Validation data for 6 lang-English in corpus_v2 folder
          
          Russian-English
          Italian-English
          Spanish-English
          Portugese-English
          German-English
          Dutch-English
         

Test data with Gold References and Generated Candidate present in testdatawithtranslations

          All 6 lang-pairs
          Additionally Romanian-English, Ukranian-English Swedish-English
          

Requirements
                    
                    python version == 3.8.5
                    
                    pip3 install sentencepiece==0.1.96
                    pip3 install transformers==4.4.0
                    

Many-To-One multilingual Poetic models
                    
                    https://huggingface.co/TuhinColumbia/russianpoetrymany
                    https://huggingface.co/TuhinColumbia/spanishpoetrymany
                    https://huggingface.co/TuhinColumbia/portugesepoetrymany
                    https://huggingface.co/TuhinColumbia/italianpoetrymany
                    https://huggingface.co/TuhinColumbia/germanpoetrymany
                    https://huggingface.co/TuhinColumbia/dutchpoetrymany
                    
Language Family specific models



To translate any given language to english

                    python translate.py

