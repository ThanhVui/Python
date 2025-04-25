# Import Library
import cloudscraper
import json
import matplotlib.pyplot as plt

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

# Task 3:


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
    axis_bar.set_xlabel("Title of Colors")
    axis_bar.set_ylabel("Number hearts of Colors")
    axis_bar.grid(True, axis='x')
    axis_bar.tick_params(axis='y', labelsize=9)
    
    for index, value in enumerate(bars):
        width = value.get_width()
        axis_bar.text(width + max(x_title_bar) * 0.01, value.get_y() + value.get_height() / 2, str(x_title_bar[index]), va='center')
    
    plt.tight_layout()
    plt.show()

# Question 3:

# Question 4:

# Question 5:
def main():
    # Question 1:
    data = fetch_top_rated_colors()
    
    # Question 2:
    visualize_color_trends(data)
    
    # Question 3:
    
    # Question 4:
    
    # Question 5:
    
# Main
if __name__ == '__main__':
    main()