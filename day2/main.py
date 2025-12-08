import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_google_api_key():
    """
    Get the Google API key from the environment variables.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Google API Key not found. Please create a .env file and set the GOOGLE_API_KEY.")
    return api_key


def generate_pitch():
    """
    Generates a hackathon pitch idea using web search context and the Gemini API directly.
    """
    try:
        # Setup 
        api_key = get_google_api_key()
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('models/gemini-2.5-flash')


        # Web Search contents 
        hackathon_theme = "Taking Humans to Mars"
        web_search_context = """
        Recent advancements in Mars colonization technology focus on sustainability and in-situ resource utilization (ISRU).
        - **Propulsion:** Nuclear thermal and electric propulsion are being developed to reduce travel time. SpaceX's Starship aims for reusable transport. A new fusion engine concept could cut trips to 4 months.
        - **Habitat:** 3D printing habitats using Martian soil (regolith) is a key area. Scientists are also exploring using microbes to biomineralize regolith into concrete, a process that could also produce oxygen. Inflatable modules and natural lava tubes are considered for radiation shielding.
        - **ISRU:** The MOXIE experiment on the Perseverance rover successfully produced oxygen from the Martian CO2 atmosphere. Water recycling systems like CHRSy are aiming for 100% efficiency.
        - **Power:** Portable nuclear fission power systems are being developed for reliable energy, crucial during long Martian dust storms.
        - **Communication:** Laser-based communication systems are in development for faster data transfer between Mars and Earth.
        - **Robotics & AI:** AI is crucial for autonomous navigation and data analysis. The success of the Ingenuity helicopter has opened possibilities for aerial scouting.
        """

        # --- Brainstorming LLM  - Prompt ---
        prompt = f"""
        You are an expert Hackathon Pitch Idea Generator. Your goal is to create a compelling and innovative project idea based on a given theme and web research.

        **Hackathon Theme:** {hackathon_theme}

        **Web Research Context:**
        {web_search_context}

        **Your Task:**
        Generate a detailed and structured hackathon pitch. The pitch must be creative, feasible for a hackathon, and directly related to the provided theme and research.

        Follow this structure precisely:

        **Project Name:** (A catchy and descriptive name for the project)

        **The Problem:** (Clearly define a specific, significant problem that needs to be solved for humans on Mars, based on the context.)

        **The Solution:** (Describe your proposed solution. How does it solve the problem? What technology from the context will you use?)

        **Key Features:**
        - Feature 1: (Describe the most important feature)
        - Feature 2: (Describe another key feature)
        - Feature 3: (Describe a 'wow' feature that makes the project stand out)
        
        **TLDR : ** ( A TLDR - that basically summarise the the whole idea in no more than 3 or 4 sentences)        
        
        Maintain an cool , friendly , nerdy tone through the entire response.  
        """

        # ---Generate Content ---
        print("wait...")
        response = model.generate_content(prompt)
        
        print("\n\n--- Your Hackathon Pitch Idea ---")
        print(response.text)
        print("---------------------------------\n")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    generate_pitch()

if __name__ == "__main__":
    main()