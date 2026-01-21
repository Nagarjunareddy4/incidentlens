# IncidentLens 🔍

**AI-Powered Incident Explainer for DevOps**

## 🚩 Problem Statement

Modern observability stacks (Prometheus, Grafana) generate high volumes of raw alerts. These alerts often arrive as complex JSON payloads or cryptic PromQL expressions. During a critical incident, On-Call Engineers waste valuable minutes decoding these alerts to understand *what* is broken and *why*, delaying the Mean Time To Resolution (MTTR).

## 💡 Solution

**IncidentLens** is an intelligent middleware that bridges the gap between raw metrics and human understanding. It ingests alerts from Prometheus or Grafana, processes them using the **Google Gemini API**, and outputs a concise, human-readable explanation of the incident, complete with potential root causes and suggested remediation steps.

## 🏗️ Architecture Overview

1.  **Input Source**: Prometheus Alertmanager or Grafana triggers a webhook to IncidentLens.
2.  **API Layer (FastAPI)**: Validates and parses the alert payload.
3.  **AI Processing**: The payload is enriched and sent to the Gemini API with a specialized system prompt.
4.  **Output**: A structured, natural language summary is returned (ready for integration into Slack, PagerDuty, or a dashboard).

## 🎯 MVP Scope

*   **Webhook Receiver**: A FastAPI endpoint (`/webhook/alerts`) to accept JSON payloads from Prometheus/Grafana.
*   **LLM Integration**: Integration with Google's Gemini Pro model to analyze alert data.
*   **Contextual Analysis**: Prompt engineering to extract service names, severity, and error rates from raw data.
*   **Response Format**: Returns a JSON response containing `summary`, `root_cause_analysis`, and `suggested_actions`.

## 🛠️ Tech Stack

*   **Language**: Python 3.10+
*   **Framework**: FastAPI
*   **Server**: Uvicorn
*   **AI Model**: Google Gemini API (`google-generativeai`)
*   **Validation**: Pydantic

## 🚀 How to Run Locally

### Prerequisites
*   Python 3.10 or higher
*   A Google Cloud API Key with access to Gemini

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/your-org/incidentlens.git
    cd incidentlens
    ```

2.  **Set up a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install fastapi uvicorn google-generativeai pydantic python-dotenv
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the root directory:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```

5.  **Start the Server**
    ```bash
    uvicorn main:app --reload
    ```

6.  **Test with a Mock Alert**
    ```bash
    curl -X POST http://localhost:8000/webhook/alerts \
    -H "Content-Type: application/json" \
    -d '{
        "status": "firing",
        "labels": {
            "alertname": "HighErrorRate",
            "service": "payment-gateway",
            "severity": "critical"
        },
        "annotations": {
            "description": "Error rate is > 5% for the last 5 minutes"
        }
    }'
    ```

## 🗺️ Future Roadmap

*   **ChatOps Integration**: Push explanations directly to Slack or Microsoft Teams channels.
*   **RAG (Retrieval-Augmented Generation)**: Ingest internal runbooks and documentation to provide context-specific remediation steps.
*   **Historical Analysis**: Vector database integration to correlate current incidents with past resolved incidents.
*   **Feedback Loop**: Mechanism for engineers to rate the AI explanation to fine-tune the prompts.
