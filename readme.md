# MLOps Project: Search Relevance Algorithm with SBERT

## Project Overview
This project focuses on building a **Search Relevance Algorithm** using **Sentence-BERT (SBERT)** to improve the search experience for news articles. The implementation ensures users receive the most relevant articles based on their queries by leveraging advanced machine learning techniques and scalable deployment practices.

### Why Search Relevance Matters
Search relevance plays a crucial role in industries where vast amounts of information are available:
- **E-commerce**: Helping users find products quickly.
- **Content Platforms**: Recommending relevant videos or media.
- **News Platforms**: Delivering accurate and timely news articles based on user queries.

For instance, a user searching for "climate change" expects to see recent, credible, and specific articles related to the topic rather than unrelated or outdated content. This project aims to address such challenges in search systems.

## Project Workflow
1. **Data Preprocessing**: Clean and preprocess the dataset for tokenization, stop word removal, and normalization.
2. **SBERT Embeddings**: Use Sentence-BERT to generate semantically meaningful embeddings for news articles.
3. **ANN Indexing**: Utilize the ANNOY library for efficient approximate nearest neighbor search.
4. **Deployment**: Containerize the system using Docker and deploy on AWS with a Flask API for user interaction.

---

## Dataset
The dataset consists of **22,399 news articles** with the following attributes:
- `article_id`: Unique identifier for each article.
- `category`: Broad classification of the article.
- `subcategory`: Specific classification within the category.
- `title`: Headline summarizing the article.
- `published_date`: Publication date.
- `text`: Main body of the article.
- `source`: Source or publication of the article.

---

## Tech Stack
- **Programming Language**: Python
- **Libraries**: 
  - `pandas`, `numpy`, `spacy` for data preprocessing
  - `sentence-transformers` for generating embeddings
  - `annoy` for approximate nearest neighbor indexing
  - `flask` for API development
  - `AWS` for cloud deployment
- **Tools**:
  - Docker for containerization

---

## Implementation Steps

### 1. Data Preprocessing
- Tokenization, stop word removal, and normalization of article text.
- Handle missing values and ensure data consistency.

### 2. SBERT Training
- Generate sentence embeddings using **Sentence-BERT**.
- Capture contextual and semantic information for accurate representation.

### 3. ANNOY Indexing
- Build an **ANN Index** using the **ANNOY library** for efficient retrieval.
- Measure similarity based on cosine similarity scores.

### 4. Deployment on AWS
- Containerize the system components:
  - Flask API
  - SBERT model
  - ANNOY index
- Deploy on an AWS EC2 instance for scalability and accessibility.

---

## Flask API Functionality
The API allows users to:
1. Submit a search query.
2. Receive a list of relevant news articles ranked by semantic similarity.

Example query: 
```bash
curl -X POST http://<your-aws-ec2-ip>:<port>/search \
-H "Content-Type: application/json" \
-d '{"query": "climate change"}'
```
Response:
```json
{
  "results": [
    {"title": "Impact of Climate Change on Global Ecosystems", "source": "BBC", "date": "2023-06-10"},
    {"title": "Recent Policies to Combat Climate Change", "source": "NY Times", "date": "2023-05-15"}
  ]
}
```

---

## Results
- **Search Relevance**: Improved retrieval of relevant news articles based on user queries.
- **Performance**: Efficient search using ANNOY for large datasets.
- **Scalability**: Seamless deployment on AWS ensures the system can handle high user loads.

---

## How to Run the Project
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mlops-search-relevance.git
cd mlops-search-relevance
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask API Locally
```bash
python app.py
```

### 4. Build and Deploy Docker Containers
```bash
docker build -t search-relevance .
docker run -p 5000:5000 search-relevance
```

### 5. Deploy on AWS
- Follow the [AWS deployment guide](https://aws.amazon.com/quickstart/) to set up your EC2 instance and deploy the containers.

---

## Folder Structure
```
mlops-search-relevance/
├── data/                 # Dataset
├── models/               # Pretrained SBERT model
├── api/                  # Flask API code
├── docker/               # Dockerfiles for deployment
├── notebooks/            # Jupyter notebooks for experimentation
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

---

## Future Scope
- **Advanced Ranking Algorithms**: Incorporate re-ranking techniques to further enhance search relevance.
- **Integration with Other Platforms**: Extend the API for use in e-commerce or other content platforms.
- **Real-time Updates**: Enable dynamic indexing for continuously updated datasets.

---

## Contact
Feel free to reach out for any questions or collaboration opportunities!
- **Email**: yourname@example.com
- **LinkedIn**: [your-linkedin-profile](https://linkedin.com/in/yourprofile)
