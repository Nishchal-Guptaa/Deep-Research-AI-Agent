# Research and Synthesis Agent

This is a Streamlit-based application that integrates with the Tavily API to perform research and synthesize information based on user queries. The application has two main phases: **Research** and **Synthesis**, helping users gather and process information effectively.

## Features

- **Search with Tavily API**: Uses Tavily to fetch relevant search results based on user queries.
- **Retry Mechanism**: Handles API rate limits with an exponential backoff mechanism.
- **Synthesis of Information**: Combines research results to generate a coherent and comprehensive response.
- **Streamlit Interface**: Provides an interactive and user-friendly interface for input and output.

## Prerequisites

- Python 3.8 or higher
- [Streamlit](https://streamlit.io/) installed
- A Tavily API key
- A `.env` file containing the Tavily API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nishchal-Guptaa/Deep-Research-AI-Agent.git
   cd Deep-Research-AI-Agent
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory with the following content:
   ```env
   api_key_tavily=your_tavily_api_key
   ```

   Replace `your_tavily_api_key` with your Tavily API key.

4. Update the `path_env` variable in the script to reflect the actual path of your `.env` file.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Enter your query in the input box and click "Generate Response."

3. The app will perform the following:
   - **Research**: Fetch relevant search results using the Tavily API.
   - **Synthesis**: Process the research results and generate a meaningful response.

4. The final response will be displayed in the Streamlit app.

## Code Overview

### Key Components

- **Tavily Search Integration**: 
  - `TavilySearchResults` is used to fetch search results.
  - Implements a retry mechanism to handle API rate limits.

- **Research Function**:
  - Gathers search results and formats them for synthesis.

- **Synthesis Function**:
  - Uses a prompt template (`ChatPromptTemplate`) to structure the synthesized response.

- **Agent Workflow**:
  - Combines research and synthesis phases.
  - Maintains state using the `AgentState` class.

- **Streamlit Interface**:
  - Takes user input and displays the generated response.

### Example Workflow

1. **Input Query**: User provides a query via the Streamlit UI.
2. **Research Phase**: 
   - Query is sent to the Tavily API.
   - Handles rate limits with retries.
   - Formats search results for the next phase.
3. **Synthesis Phase**:
   - Combines search results into a coherent response using a prompt template.
4. **Output**:
   - Displays the synthesized response in the Streamlit app.

## Dependencies

- `langchain_core`
- `langchain_community`
- `streamlit`
- `python-dotenv`

Install these dependencies using:
```bash
pip install langchain-core langchain-community streamlit python-dotenv langchain
```

## File Structure

```
.
├── app.py              # Main application script
├── requirements.txt    # List of Python dependencies
├── .env                # Environment file with API key
```

## Notes

- Ensure the `.env` file is correctly configured with your Tavily API key.
- The retry mechanism handles Tavily API rate limits, but excessive usage may still result in errors.


## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Contact

For questions or support, please contact `Nishchal-Guptaa`.
