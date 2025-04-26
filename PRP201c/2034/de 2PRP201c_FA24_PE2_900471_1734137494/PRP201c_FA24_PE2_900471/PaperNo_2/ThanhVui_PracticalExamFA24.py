# Import Library
import cloudscraper
import json
import matplotlib.pyplot as plt
import sqlite3

# Question 1:
# Task 1:
class ColorPalette:
    def __init__(self, ID, Title, UserName, HEXCode, RGBValues, HSVValues, NumberOfVotes, NumberOfHeads):
        self.ID = ID
        self.Title = Title
        self.UserName = UserName
        self.HEXCode = HEXCode
        self.RGBValues = RGBValues
        self.HSVValues = HSVValues
        self.NumberOfVotes = NumberOfVotes
        self.NumberOfHeads = NumberOfHeads
    
# Task 2:
def fetch_top_rated_colors():
    url_api = 'https://www.colourlovers.com/api/colors/top?format=json'
    list_colors = []
    
    try:
        scraper = cloudscraper.create_scraper()
        responses = scraper.get(url_api)
        responses.raise_for_status()
        
        data = responses.json()
        print(json.dumps(data, indent=4))
        
        count = 0
        for row in data:
            color_palette_object = ColorPalette(
                row['id'],
                row['title'],
                row['userName'],
                row['hex'],
                row['rgb'],
                row['hsv'],
                row['numVotes'],
                row['numHearts']
            )
            list_colors.append(color_palette_object)
            count += 1
        print(f"Load successfully color {count} objects!")
        
    except Exception as e:
        print(f"Error while handling fetch API: {e}")
    return list_colors

# Task 3: Discuss advantages and challenges of splitting RGB and HSV into individual attributes
"""
Advantages of Splitting RGB and HSV into Individual Attributes:
1. Direct Access: Storing RGB (red, green, blue) and HSV (hue, saturation, value) as individual attributes
   allows direct access.
2. Type Safety: Individual attributes can be explicitly typed, reducing the risk of errors
   from dictionary key typos or unexpected dictionary structures.
3. Readability: The class structure is more intuitive, as each attribute represents a distinct property of the
   color, making the code easier to understand and maintain.

Challenges of Splitting RGB and HSV into Individual Attributes:
1. Increased Complexity in Class Definition: The ColorPalette class has more attributes (10 instead of 6 if
   RGB and HSV were kept as dictionaries), which makes the class definition and instantiation more verbose.
2. Data Consistency: If RGB or HSV values are updated, you must ensure all related attributes (e.g., red, green,
   blue) are updated together, which can lead to errors if not handled carefully.
3. Scalability: If the API adds new color spaces (e.g., CMYK), you’d need to add more attributes to the class,
   increasing maintenance overhead. Keeping RGB and HSV as dictionaries would make the class more flexible for such
   changes.
4. Memory Usage: Storing each value as a separate attribute may use slightly more memory compared to a single
   dictionary, though this is negligible for small datasets.
"""

# Question 2:
def visualize_color_trends(data):    
    fig, (axis_line, axis_bar) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Line chart
    number_votes_colors = {}
    for color_palette_object in data:
        number_votes_colors[color_palette_object.Title] = color_palette_object.NumberOfVotes
    print(number_votes_colors)
    
    # Get top 5 colors the most votes
    top_5_colors = sorted(number_votes_colors.items(), key=lambda x: x[1], reverse=True)[:5]
    print(top_5_colors)
    
    x_title = [title[0] for title in top_5_colors]
    y_vote = [vote[1] for vote in top_5_colors]
    
    axis_line.plot(x_title, y_vote, marker='o')
    axis_line.set_title("The number of votes with top 5 colors")
    axis_line.set_xlabel("Title of Colors")
    axis_line.set_ylabel("Number Votes of Colors")
    axis_line.grid(True)
    axis_line.tick_params(axis='x', rotation=45)
    
    for index, value in enumerate(y_vote):
        axis_line.text(index, value + max(y_vote) * 0.02, str(value), ha='center')
    
    # Bar chart
    all_colors = sorted(number_votes_colors.items(), key=lambda x: x[1], reverse=True)
    print(all_colors)
    
    x_title_bar = [title[1] for title in all_colors]
    y_vote_bar = [vote[0] for vote in all_colors]
    
    bars = axis_bar.barh(y_vote_bar, x_title_bar, color='green')
    axis_bar.set_title("The number of hearts of all colors")
    axis_bar.set_xlabel("Number hearts of Colors")
    axis_bar.set_ylabel("Title of Colors")
    axis_bar.grid(True, axis='x')
    axis_bar.tick_params(axis='y', labelsize=9)
    
    for index, value in enumerate(bars):
        width = value.get_width()
        axis_bar.text(width + max(x_title_bar) * 0.01, value.get_y() + value.get_height() / 2, str(x_title_bar[index]), va='center')
    
    plt.tight_layout()
    plt.show()
    
# Task 2: Discuss advantages and challenges of using visualizations
"""
Advantages of Using Visualizations to Identify Popularity Trends:
1. Quick Insights: Visualizations like line and bar charts allow users to quickly identify trends, such as which
   colors have the most votes or hearts, without needing to analyze raw numbers.
2. Comparative Analysis: The line chart makes it easy to compare the top 5 colors’ votes, while the horizontal
   bar chart shows the distribution of hearts across all colors, highlighting disparities.
3. Engagement: Visual representations are more engaging and intuitive for users compared to tables or raw data,
   making it easier to communicate findings.

Challenges of Using Visualizations to Identify Popularity Trends:
1. Data Overload: With many colors, the horizontal bar chart can become cluttered, making it hard to read labels
   or distinguish bars, especially if the number of colors increases significantly.
2. Misleading Scales: If the scales of votes or hearts vary widely (e.g., one color has 1500 votes, others have
   10), the line chart might exaggerate differences, or the bar chart might compress smaller values, leading to
   misinterpretation.   
3. Label Overlap: In the line chart, long color titles may overlap when rotated, reducing readability. The bar
   chart’s y-axis labels may also become unreadable if there are too many colors.
4. Static Nature: These visualizations are static snapshots. If the data changes frequently (e.g., new votes),
   the charts need to be regenerated, which may not be efficient for real-time analysis.
"""

# Question 3:
def store_top_colors_in_database(data):
    try:
        # Create database
        with sqlite3.connect('TopColors.db') as conn:
            cursor = conn.cursor()
            
            # Create table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS TopColors(
                    ID TEXT PRIMARY KEY,
                    Title TEXT NOT NULL,
                    UserName TEXT NOT NULL,
                    HEXCode TEXT NOT NULL,
                    RGB_Red INTEGER NOT NULL,
                    RGB_Green INTEGER NOT NULL,
                    RGB_Blue INTEGER NOT NULL,
                    HSV_Hue INTEGER NOT NULL,
                    HSV_Saturation INTEGER NOT NULL,
                    HSV_Value INTEGER NOT NULL,
                    Votes INTEGER NOT NULL,
                    Hearts INTEGER NOT NULL
                )               
            """)
            
            # Count 
            count = 0
            # Insert data into table
            for color in data:
                cursor.execute("""
                    INSERT OR IGNORE INTO TopColors(ID, Title, UserName, HEXCode, RGB_Red, RGB_Green, RGB_Blue, HSV_Hue, HSV_Saturation, HSV_Value, Votes, Hearts)    
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)  
                """, (color.ID,
                    color.Title,
                    color.UserName,
                    color.HEXCode,
                    color.RGBValues["red"],
                    color.RGBValues["green"],
                    color.RGBValues["blue"],
                    color.HSVValues["hue"],
                    color.HSVValues["saturation"],
                    color.HSVValues["value"],
                    color.NumberOfVotes,
                    color.NumberOfHeads))
                count += 1
            print(f"Insert into table {count} colors successfully!")
            
            # Display top 3 colors
            cursor.execute("""
                SELECT ID, Title, Votes, Hearts
                FROM TopColors
                ORDER BY Votes DESC
                LIMIT 3                
            """)
            top_3_colors = cursor.fetchall()
            print("\nTop 3 Colors:")
            if top_3_colors:
                for color in top_3_colors:
                    print(f"Color: {color[1]}")
            else:
                print("Not Found Data!")
            
            # Average colors
            cursor.execute("""
                SELECT AVG(Votes)
                FROM TopColors
                WHERE Hearts > 10               
            """)
            avg_color = cursor.fetchone()
            
            print("\nThe Average of colors")
            if avg_color and avg_color[0] is not None:
                print(f"Average of color: {round(avg_color[0], 2)}")
            else:
                print(f"Not found data of average of color!")
            
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error while handling sql: {e}")
    except Exception as ex:
        print(f"Exception error: {ex}")
    
# Question 4:
# Task 1:
def category_color_popularity():
    try:
        # Create database
        with sqlite3.connect('TopColors.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""PRAGMA table_info(TopColors)""")
            existing_column = [row[1] for row in cursor.fetchall()]
            
            if 'PopularityLevel' not in existing_column:
                # Add column
                cursor.execute("""
                    ALTER TABLE TopColors ADD COLUMN PopularityLevel TEXT CHECK (PopularityLevel IN ('High', 'Low', 'Moderate'))
                """)
            
            # Update table with add column
            cursor.execute("""
                UPDATE TopColors
                SET PopularityLevel =
                    CASE
                        WHEN votes > 20 THEN 'High'
                        WHEN votes > 10 AND votes < 20 THEN 'Moderate'
                        ELSE 'Low'
                    END
            """)
            print("\nUpdate PopularityLevel successfully!")
            
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error while handling sql: {e}")
    except Exception as ex:
        print(f"Exception error: {ex}")
        
# Task 2: Discuss the potential challenges of using static thresholds for dynamic popularity
    """
    Challenges of Using Static Thresholds for Dynamic Popularity Trends:

    1. Inflexibility to Data Distribution:
       - Static thresholds (e.g., >20 for High, 10–20 for Moderate, <10 for Low) may not reflect the actual
         distribution of votes in the dataset. For example, in this dataset, most colors have votes in the
         hundreds or thousands (e.g., 1532, 1149, 1122), so all colors are categorized as 'High', making the
         categorization less meaningful. A better approach might be to use percentiles (e.g., top 25% as High,
         next 50% as Moderate, bottom 25% as Low) to adapt to the data.

    2. Sensitivity to Outliers:
       - If there are outliers (e.g., one color with 10,000 votes while others have <100), static thresholds
         can skew the categorization. Most colors might be categorized as 'Low' or 'Moderate', even if they
         have significantly more votes than others in those categories. Normalizing the votes or using relative
         thresholds could mitigate this issue.

    3. Temporal Changes:
       - Popularity trends may change over time as more users vote. A color with 20 votes might be 'High' today
         but 'Low' in the future if vote counts increase significantly. Static thresholds don’t adapt to these
         changes, requiring manual updates. A dynamic system that recalculates thresholds periodically would be
         more robust.

    4. Arbitrary Threshold Selection:
       - The choice of 10 and 20 as thresholds is arbitrary and may not be meaningful for all datasets. In a
         highly active community, 20 votes might be insignificant, while in a smaller community, 10 votes might
         be substantial. Thresholds should be chosen based on domain knowledge or statistical analysis of the data.

    5. Loss of Granularity:
       - The three categories (High, Moderate, Low) oversimplify popularity. For example, colors with 21 votes
         and 1500 votes are both 'High', but their popularity differs greatly. This can obscure nuanced insights.
         A more granular system, such as a numerical popularity score or additional categories (e.g., 'Very High'),
         might provide more detailed information.
    """
    
# Question 5 Function:
def summary_colors_popularity_level():
    # Summary colors popularity level
    try:
        # Create database
        with sqlite3.connect('TopColors.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT Title, Votes, PopularityLevel
                FROM TopColors
                ORDER BY Votes DESC
                LIMIT 3             
            """)
            # Top 3 Colors
            top_color = cursor.fetchall()
            print("\nTop 3 colors popularity level")
            for row in top_color:
                print(f"Title: {row[0]}, Votes: {row[1]}, PopularityLevel: {row[2]}")
            
            # Summary    
            cursor.execute("""
                SELECT PopularityLevel, COUNT(PopularityLevel)
                FROM TopColors
                GROUP BY PopularityLevel               
            """)
            
            # Summary color popularity level
            summary_color = cursor.fetchall()
            print("\nSummary colors popularity level")
            for row in summary_color:
                print(f"Popularity: {row[0]}, Count: {row[1]}")
                
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error while handling sql: {e}")
    except Exception as ex:
        print(f"Exception error: {ex}")
        
# Question 5:
def main():
    # Question 1:
    data = fetch_top_rated_colors()
    
    # Question 2:
    visualize_color_trends(data)
    
    # Question 3:
    store_top_colors_in_database(data)
    
    # Question 4:
    category_color_popularity()
    
    # Question 5:
    summary_colors_popularity_level()
    
# Main
if __name__ == '__main__':
    main()