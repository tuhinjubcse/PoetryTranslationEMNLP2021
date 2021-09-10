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
                    pip3 install datasets==1.4.1
                    pip3 install bert_score==0.3.8
                    
                    

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


To finetune MBART-50 many-to-one model run
                    
                    sh finetunemulti.sh
                    Edit  line 62 to set rootdir to access data file /transformers/examples/seq2seq/run_translation.py

To finetune MBART-50 many-to-one on language-family-specific data or only on one language set the dataflags to False in run_translation.py

                                   spanish = True
                                   portugese = True
                                   russian = True
                                   german = True
                                   italian = True
                                   dutch = True


To evaluate use following files, please edit language and mode
                                        
                                        calculate-bs.py
                                        calculate-bleu.py
