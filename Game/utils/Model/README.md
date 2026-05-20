This document details how the game's mechanics were reduced to a Machine Learning problem using Natural Language Inference (NLI) and a dual-model pipeline.

---

## 🏗️ The Hybrid Dual-Model System

To optimize performance and latency, the game splits processing between a heavy cloud-based model and a lightweight local model.  
                    [ User Question ]  
                             │  
                             ▼  
        ┌──────────────────────────────┐  
        │  Auxiliary Model (Local)     │  
        │  Checks hidden key facts     │  
        └──────────────┬───────────────┘  
                       │  
                       ▼  
        Did the user uncover a key fact?  
                 │  
        ┌────────┴────────┐  
        │                 │  
      YES                NO  
        │                 │  
        ▼                 ▼  
┌────────────────┐   ┌──────────────────────────────┐  
│ Update Progress│   │   Main Oracle (Cloud API)   │  
│ Bar + UI Popup │   │ Returns: Yes / No / Ignore  │  
└────────────────┘   └──────────────┬───────────────┘  
                                    │  
                                    ▼  
                           [ Final Response ]   
                           
### 1. The Main Oracle (Cloud)
*   **Base Model:** [DeBERTa-v3-base](https://huggingface.co/microsoft/deberta-v3-base)
*   **Deployment:** Hosted as an API via [Hugging Face Spaces](https://huggingface.co/).
*   **Function:** This is the main model that powers the question answering. It accepts a thorough, secret description of a scenario as the *passage*, and the player's text input as the *question*, predicting whether the statement holds true.

### 2. The Auxiliary Progress Tracker (Local Edge)
*   **Base Model:** [xtremedistil-l6-h256-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased)
*   **Optimization:** Quantized and converted to **TensorFlow Lite (TFLite)** to reach a final disk size of just **12.4MB**.
*   **Function:** This model scans user questions to see if they have successfully deduced any of the pre-defined milestones required to progress or unlock new chapters.

---

## 🔄 Algorithmic Approach: Inverting NLI for State Tracking

Standard NLI models evaluate a `Passage` and a `Hypothesis` to output labels like *Entailment*, *Neutral*, or *Contradiction*. 

For this training pipeline, *Neutral* and *Contradiction* were merged into a single binary **"No"** label (adjusting class weights during training to handle the dataset shift).

### How State Tracking Works Interactively:
To track milestones without forcing the user to type an exact phrase, the traditional NLI inputs for the local model were inverted:
*   **Passage Input =** The player's question.
*   **Hypothesis Input =** A hidden key fact (e.g., *"Albert was on a cruise ship"*).

If the model predicts **Entailment (Yes)**, then the player's question implies they have discovered that specific piece of the puzzle. This triggers a progress update in the UI, and gives a hint explanation to the user.

