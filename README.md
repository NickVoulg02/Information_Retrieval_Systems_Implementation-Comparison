# Information Retrieval Systems: Implementation and Comparison of VSM and ColBERT

This project explores **Information Retrieval (IR) models** by implementing and comparing two fundamental approaches:  
- **Vector Space Model (VSM)** with custom term-weighting (TF-IDF)  
- **ColBERT** (Contextualized Late Interaction over BERT), a modern deep-learning based retrieval model  

The study uses the **Cystic Fibrosis dataset**, which contains **1,209 documents** and **100 queries** (with a provided subset of 20 queries).  

The goal is to build working search engines for the dataset, evaluate their performance using standard IR metrics, and gain insight into the trade-offs between traditional and neural retrieval methods.

---

## 📂 Repository Contents
- `inverted_index.py` – Implementation of the inverted index used for VSM  
- `vector_space_model.py` – VSM implementation with TF-IDF weighting  
- `metrics.py` – Evaluation metrics (MAP, MRR) for model comparison  
- `preprocess.py` – Preprocessing for ColBERT (generates TSV files for documents & queries)  
- `colbert_test_link.ipynb` – Notebook for running ColBERT experiments (Google Colab compatible)  
- `docs/` – Document collection (1,209 files)  
- `Queries_20` – Subset of 20 queries for evaluation  
- `Relevant_20` – Ground-truth relevance judgments  

---

## ⚙️ Implementation Details

### 🔹 Inverted Index
- Constructed from the `docs/` collection  
- Removes **stopwords** (NLTK) and **numeric tokens**  
- Stores `(doc_id, frequency)` pairs for each term  

### 🔹 Vector Space Model (VSM)
- **TF weighting**: `log(1 + fᵢⱼ / |doc|)`  
- **IDF weighting**: `log(1 + N / nᵢ)`  
- Document-term matrix stored in `vector_space2.csv`  
- Queries represented in the same vector space  
- **Cosine similarity** used for ranking  

### 🔹 ColBERT
- Based on **BERT embeddings** with late interaction  
- Uses Hugging Face Transformers library  
- Documents and queries encoded into contextualized embeddings  
- Indexed and searched with ColBERT checkpoint  
- Implemented via **Google Colab Notebook** (`colbert_test_link.ipynb`)  

---

## 📊 Evaluation

Two **order-aware IR metrics** were used:  
- **Mean Average Precision (MAP)** – Evaluates precision at multiple ranks  
- **Mean Reciprocal Rank (MRR)** – Evaluates position of the first relevant result  

### Key Findings
- **VSM outperformed ColBERT** on this dataset in terms of MAP and MRR.  
- Likely due to query formulation: VSM emphasizes **term matching**, while ColBERT is designed for **semantic similarity**.  
- ColBERT would be expected to perform better on queries requiring deeper contextual understanding.  

---

## 🚀 Usage

### 1. Clone the Repository
```bash
git clone https://github.com/NickVoulg02/Information-Retrieval.git
cd Information-Retrieval
```

### 2. Run VSM
```bash
python vector_space_model.py
python metrics.py
```

### 3. Run ColBERT
- Open `colbert_test_link.ipynb` in Google Colab  
- Upload/generated TSV files (`doc_col.tsv`, `queries_20.tsv`)  
- Run cells to build index and retrieve results  

---

## 📈 Results
Plots comparing VSM and ColBERT performance (MAP & MRR) are included in the report.  

Summary:  
- **VSM achieved higher MAP and MRR** on this dataset.  
- **ColBERT remains competitive** and could excel in datasets with semantically complex queries.  

---

## 📚 References
- Salton, G., Buckley, C. (1988). *Term-weighting Approaches in Automatic Text Retrieval*. Inf. Process. Manage.  
- Salton, G., Wong, A., Yang, C.S. (1975). *A Vector Space Model for Automatic Indexing*. Commun. ACM.  
- [Breaking Down Mean Average Precision (mAP)](https://towardsdatascience.com/breaking-down-mean-average-precision-map-ae462f623a52)  
- [Mean Reciprocal Rank (MRR)](https://en.wikipedia.org/wiki/Mean_reciprocal_rank)  

---

## 👨‍💻 Author
**Nikolaos Voulgaris**  
Department of Computer Engineering & Informatics, University of Patras  
[GitHub Repository](https://github.com/NickVoulg02/Information-Retrieval)  
