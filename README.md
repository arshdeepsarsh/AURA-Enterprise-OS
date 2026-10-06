# AURA Enterprise OS — Cognitive ERP & Forensic AI Auditor

![Java](https://img.shields.io/badge/Core-Java_Spring_Boot-green?logo=spring)
![Python](https://img.shields.io/badge/Brain-Python_3-blue?logo=python)
![AI](https://img.shields.io/badge/AI_Engine-Google_Gemini-orange?logo=google)
![Database](https://img.shields.io/badge/Database-Supabase_PostgreSQL-3ecf8e?logo=supabase)
![Vectors](https://img.shields.io/badge/Memory-pgvector-purple)
![Status](https://img.shields.io/badge/Project-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

AURA Enterprise OS is a next-generation Cognitive Enterprise Resource Planning (ERP) system. It moves beyond passive data storage by integrating a deterministic Java business ledger with an autonomous, reasoning AI Brain powered by Large Language Models (LLMs).

This project demonstrates an advanced dual-stack architecture where a Python AI agent communicates directly with a Java Spring Boot backend across local network ports, persisting complex operational data and high-dimensional vector mathematics to a unified Supabase cloud database.

--- 

## 🎯 Project Objective

The primary goal of AURA is to design and implement an intelligent, autonomous corporate framework that can:
* Replace manual compliance reviews with an autonomous LLM agent that reasons through unstructured enterprise data (like vendor invoices).
* Maintain a mathematically rigid, secure, and ACID-compliant business ledger using Java Spring Boot and Hibernate JPA.
* Generate and store high-dimensional semantic embeddings of corporate contracts using `pgvector` for advanced enterprise search.
* Serve as an elite final-year engineering portfolio piece demonstrating cross-language microservice communication, cloud database integration, and applied AI.

---

## 🚀 Key Features

* **Cognitive LLM Auditor:** A Python-based AI agent (`aura-brain`) utilizing the Google Gemini API to autonomously fetch pending invoices, analyze risk factors (e.g., suspicious vendors, threshold violations), and dynamically update compliance statuses.
* **Secure Enterprise Ledger:** A Java Spring Boot REST API (`aura-core`) enforcing strict data entity rules, managing HTTP traffic, and securely interfacing with the cloud database.
* **Cloud Vector Memory:** Integration with Supabase PostgreSQL, utilizing the `pgvector` extension to store 768-dimensional AI embeddings representing legal contracts and documents.
* **Cross-System Communication:** Full-stack integration where the Python AI and Java server continuously pass structured JSON payloads to each other via HTTP POST and PATCH requests.
* **Automated Data Persistence:** Hibernate-driven automated table generation and Row-Level Security (RLS) bypass mechanics for seamless developer iteration.

---

## 🧠 Practical Use Cases

* **Autonomous Financial Compliance:** Automatically flagging high-value or suspicious invoices for manual human review without requiring an analyst to read every document.
* **Intelligent Document Forensics:** Creating searchable semantic maps of corporate contracts, allowing users to find clauses based on "meaning" rather than exact keyword matches.
* **Microservice Architecture Demonstration:** Showcasing how enterprise environments separate heavy Machine Learning workloads (Python) from secure, transactional business logic (Java).

---

## 🏗️ High-Level System Architecture

AURA follows a separated-concern microservice pattern, acting as two distinct applications sharing a single cloud memory.

### Core Layers

#### 1. The AI Layer (`aura-brain`)
* Python-based intelligent agent.
* Integrates `google-generativeai` for LLM reasoning and `numpy` for vector mathematics.
* Contains autonomous loops (`audit_agent.py`) that fetch data from the Core, process it, and send decisive updates back.

#### 2. The Logic Layer (`aura-core`)
* Java Spring Boot providing a secure RESTful API.
* Implements the Controller-Repository-Entity pattern to govern database interactions.
* Handles data validation, auto-timestamping, and connection pooling via HikariCP.

#### 3. The Memory Layer (Supabase Database)
* Hosted PostgreSQL instance functioning as the Single Source of Truth.
* Stores deterministic business data (`invoices`) alongside probabilistic AI data (`documents` with vector embeddings).

---

## 📁 Project Structure

```text
AURA-Enterprise-OS/
│
├── aura-brain/                     # Python AI & Machine Learning Engine
│   ├── .env                        # Secret Keys (Ignored in Git)
│   ├── audit_agent.py              # Autonomous Gemini LLM auditor script
│   ├── main.py                     # Document vector embedding script
│   ├── send_invoice.py             # HTTP Bridge script to send dummy data to Java
│   └── requirements.txt            # Python dependencies
│
├── aura-core/                      # Java Spring Boot Enterprise Ledger
│   └── core/
│       ├── .mvn/
│       ├── src/
│       │   └── main/
│       │       ├── java/com/aura/core/
│       │       │   ├── CoreApplication.java         # Spring Boot Entry Point
│       │       │   ├── HealthController.java        # System diagnostics API
│       │       │   ├── Invoice.java                 # JPA Database Entity
│       │       │   ├── InvoiceController.java       # REST API Endpoints
│       │       │   └── InvoiceRepository.java       # Database Access Object
│       │       │
│       │       └── resources/
│       │           └── application.properties       # Supabase JDBC Config
│       │
│       ├── mvnw                    # Maven Wrapper (Linux/Mac)
│       ├── mvnw.cmd                # Maven Wrapper (Windows)
│       └── pom.xml                 # Java dependencies
│
└── .gitignore                      # Security and build-artifact exclusions
