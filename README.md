# SafeHaven API

![Status](https://img.shields.io/badge/status-in_development-blue)

A secure and anonymous backend system designed to support users on their journey toward emotional healing, mental wellness, and spiritual growth.

## ✨ Project Vision
SafeHaven API is a privacy-first Django backend platform that empowers users—especially students—facing anxiety, depression, trauma, or emotional stress. Through tools like journaling, mood tracking, gratitude logging, and access to supportive therapists and community reflections, the system fosters:
    Emotional resilience
    Mindfulness and spiritual grounding
    Healing from childhood trauma
   Purpose discovery and personal growth
All interactions are anonymous, ensuring a safe space for reflection and healing.
Importantly, the platform also addresses non-suicidal emotional struggles—such as the pain of family divorce, childhood neglect, addiction, and identity confusion. These experiences often go unspoken, yet they deeply affect mental health and spiritual well-being.

## 🚀 Core Features

This project is currently in development. The features are broken down into what has been implemented and what is planned for future development.

#### ✅ Implemented

*   **Secure Token-Based Authentication:** Ensures complete privacy and user anonymity.
*   **Anonymous Journal:** A secure API for users to create and view their private journal entries.

#### 📅 Planned

*   **Mood Tracker:** API for daily mood entries with emotional tags and triggers.
*   **Gratitude Log:** API for encouraging reflection on positive aspects of life.
*   **Daily Affirmations:** An endpoint to deliver uplifting messages to inspire and motivate.
*   **Grounding Activities Log:** Endpoints to track practices like breathwork, walking, and prayer.
*   **Therapist Directory:** A protected endpoint to list vetted therapists.
*   **Community Reflection Board:** An API for a safe space where users can share insights anonymously.
*   **Weekly Summary Generator:** An analytics endpoint to show mood trends and emotional patterns.
*   **Spiritual Reflection Goals:** An API to allow users to record intentions and life goals.

## 💻 Technology Stack

*   **Backend Framework:** Django
*   **API Toolkit:** Django REST Framework
*   **Database:** SQLite3 (for development)

## ⚙️ Local Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/edomcode/safehaven-api.git
    cd safehaven-api
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    *(A `requirements.txt` file will be added soon)*

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser for testing:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```