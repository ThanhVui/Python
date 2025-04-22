import sqlite3
import cloudscraper

import matplotlib.pyplot as plt 
# Q1 
class ColorPalette: 
    def __init__(self, ID, title, userName, hexCode, rgbValues, hsvValues, numberOfVotes , numberOfHearts):
        self.ID = ID
        self.title = title
        self.userName = userName
        self.hexCode = hexCode
        self.rgbValues = rgbValues
        self.hsvValues = hsvValues
        self.numberOfVotes = numberOfVotes
        self.numberOfHearts = numberOfHearts
    
    def __str__(self):
        return f"Title: {self.title}\nUser: {self.userName}\nHex: {self.hexCode}\nVotes: {self.numberOfVoteAndHearts}"

def fetch_top_rated_colors(): 
    print("==========Q1==========")
    data = []
    apiUrl = "https://www.colourlovers.com/api/colors/top?format=json"


    """ data mẫu của 1 phần tử trong list dataInRespone
        {"id":14,"title":"Black","userName":"ninjascience","numViews":157676,"numVotes":1532,"numComments":1789,"numHearts":4.5,"rank":1,"dateCreated":"2004-12-17 08:36:26","hex":"000000",
        "rgb":{"red":0,"green":0,"blue":0},"hsv":{"hue":0,"saturation":0,"value":0},"description":"<a href=\"http:\/\/www.colourlovers.com\/color\/69636F\/Store_me_Storm\" target=\"_blank\"><img src=\"http:\/\/static.colourlovers.com\/images\/colors\/2618\/2618826i.jpg\" \/><\/a><a href=\"http:\/\/www.colourlovers.com\/color\/A79DA9\/Not_Flying_Elephant\" target=\"_blank\"><img src=\"http:\/\/static.colourlovers.com\/images\/colors\/2620\/2620182i.jpg\" \/><\/a>\r\n<div style=\
        max-width: 400px ;margin-left: auto; margin-right: auto; text-align: center; color:#ebf2f5; border: 4px dotted #6b6b6b; font-size:112%; font-family:palatino linotype, palatino, serif; line-height:1.5; padding:12px; background-color: #1b1b1f; background-image: -moz-linear-gradient(top, #1b1b1f, #31314a); background-image: -webkit-gradient(linear,left top,left bottom,color-stop(0, #1b1b1f),color-stop(1, #31314a)); filter: progid:DXImageTransform.Microsoft.gradient(startColorStr=","url":"http:\/\/www.colourlovers.com\/color\/000000\/Black","imageUrl":"http:\/\/www.colourlovers.com\/img\/000000\/100\/100\/Black.png","badgeUrl":"http:\/\/www.colourlovers.com\/images\/badges\/c\/0\/14_Black.png","apiUrl":"http:\/\/www.colourlovers.com\/api\/color\/000000"}
    """
    try:
        # Sử dụng cloudscraper thay vì requests để vượt qua Cloudflare
        scraper = cloudscraper.create_scraper()
        response = scraper.get(apiUrl)

        # nếu có lỗi http thì raise exception
        response.raise_for_status()
        # nếu không có lỗi http thì parse json
        dataInRespone = response.json()  # bây h dataInRespone là 1 list các dict data của top rated colors

        # nếu không có lỗi json thì tạo các đối tượng ColorPalette và thêm vào danh sách data []
        count = 0 
        for color in dataInRespone:
            temptObject = ColorPalette(
                color["id"],
                color["title"],
                color["userName"],
                color["hex"],
                color["rgb"],
                color["hsv"],
                color["numVotes"],  
                color["numHearts"]
            )
            data.append(temptObject)
            count +=1 

        print(f"Sucessfully fetch {count} color from api")
        
    except Exception as e:
        print(f"Error fetching data: {e}")
    
    return data 



# Q2 

def data_visualize_color_trend(colors):
    print("==========Q2==========")
    # Tạo một figure với 2 subplots (1 hàng, 2 cột)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # ------------------ LINE CHART (top 5 màu) ------------------
    colorVoteData = {}
    for objectColorPalette in colors:
        colorVoteData[objectColorPalette.title] = objectColorPalette.numberOfVotes
    
    # Lấy top 5 màu nhiều vote nhất
    top5VotedColor = sorted(colorVoteData.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Chuẩn bị dữ liệu cho line chart
    xAxis_line = [x[0] for x in top5VotedColor]
    yAxis_line = [y[1] for y in top5VotedColor]
    
    # Vẽ line chart trên subplot đầu tiên (ax1)
    ax1.plot(xAxis_line, yAxis_line, marker='o', linewidth=2, markersize=8)
    ax1.set_title("Top 5 most voted colors", fontsize=14, fontweight='bold')
    ax1.set_xlabel("Color Names", fontsize=12)
    ax1.set_ylabel("Number of votes", fontsize=12)
    ax1.grid(True)
    ax1.tick_params(axis='x', rotation=45)
    
    # Thêm giá trị số lượng vote trên mỗi điểm
    for i, v in enumerate(yAxis_line):
        ax1.text(i, v + max(yAxis_line)*0.02, str(v), ha='center')
    
    # ------------------ HORIZONTAL BAR CHART (tất cả màu) ------------------
    # Lấy ra giá trị số và tên màu cho tất cả màu
    all_colors = sorted(colorVoteData.items(), key=lambda x: x[1], reverse=True)
    xAxis_bar = [y[1] for y in all_colors]  # Số lượng vote
    yAxis_bar = [x[0] for x in all_colors]  # Tên màu
    
    # Vẽ biểu đồ ngang trên subplot thứ hai (ax2)
    bars = ax2.barh(yAxis_bar, xAxis_bar, color='skyblue')
    ax2.set_title("All colors vote distribution", fontsize=14, fontweight='bold')
    ax2.set_xlabel("Number of hearts", fontsize=12)
    ax2.set_ylabel("Colors", fontsize=12)
    ax2.grid(True, axis='x')
    
    # Đảm bảo tên màu hiển thị đầy đủ
    ax2.tick_params(axis='y', labelsize=9)
    
    # Hiển thị giá trị trên mỗi thanh
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax2.text(width + max(xAxis_bar)*0.01, bar.get_y() + bar.get_height()/2, 
                 str(xAxis_bar[i]), va='center')
    
    # Điều chỉnh layout để đảm bảo không gian hiển thị tốt
    plt.tight_layout()
    
    # Hiển thị biểu đồ
    plt.show()


# Q3 
def createFileIfNotExist(fileName): 
    with open(fileName , 'w') as f : 
        return True

def createTableInDb(cursor):
    cursor.execute(''' CREATE TABLE IF NOT EXISTS TopColors(
                   ID TEXT PRIMARY KEY,
                   Title TEXT NOT NULL,
                   UserName TEXT NOT NULL,
                   RGB_Red INTEGER,
                   RGB_Green INTEGER,
                   RGB_Blue INTEGER,
                   HSV_Hue INTEGER,
                   HSV_Saturation INTEGER,
                   HSV_Value INTEGER,
                   Votes INTEGER NOT NULL,
                   Hearts INTEGER NOT NULL )''')

def insertDataInDb(colors, cursor):
    x = 0
    for color in colors:
        cursor.execute(''' INSERT OR IGNORE INTO TopColors(
                       ID, Title, UserName, 
                       RGB_Red, RGB_Green, RGB_Blue,
                       HSV_Hue, HSV_Saturation, HSV_Value,
                       Votes, Hearts)
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                      (color.ID, color.title, color.userName, 
                       color.rgbValues["red"], color.rgbValues["green"], color.rgbValues["blue"],
                       color.hsvValues["hue"], color.hsvValues["saturation"], color.hsvValues["value"], 
                       color.numberOfVotes, color.numberOfHearts))
        x += 1
    
    print(f"Success insert {x} elements in to database.")

def queries(cursor):
    try:
        # Query 1: Top 3 colors with highest number of votes
        cursor.execute('''SELECT t.ID, t.Title, t.Votes, t.Hearts 
                         FROM TopColors t 
                         ORDER BY Votes DESC 
                         LIMIT 3''')
        que1 = cursor.fetchall()
        
        print("Top 3 colors with highest number of votes:")
        if que1:
            print(f"{'ID':<10}{'Title':<20}{'Votes':<10}{'Hearts':<10}")
            print("-" * 50)
            for row in que1:
                print(f"{row[0]:<10}{row[1]:<20}{row[2]:<10}{row[3]:<10}")
        else:
            print("No data found.")

        # Query 2: Average votes for colors with > 10 hearts
        cursor.execute('''SELECT AVG(t.Votes) 
                         FROM TopColors t 
                         WHERE t.Hearts > 10''')
        que2 = cursor.fetchone()  # Chỉ lấy một hàng
        
        print("\nAverage number of votes for colors with > 10 hearts:")
        if que2 and que2[0] is not None:
            avg_votes = round(que2[0], 2)
            print(avg_votes)
        else:
            print("No colors found with > 10 hearts.")

    except Exception as e:
        print(f"Error executing queries: {e}")



def store_top_colors_in_database(colors): 
    print("==========Q33==========")

    # tạo sqlite db tên TopColors.db 
    createFileIfNotExist("TopColors.db")
    with sqlite3.connect("TopColors.db") as connector: 
         cursor = connector.cursor()
         createTableInDb(cursor)
         insertDataInDb(colors, cursor)
         queries(cursor)
         cursor.close()
         connector.commit()



# Q4 
def addAttributeAndRestoreToTable(cursor):
    # Step 1: Add the PopularityLevel column with the CHECK constraint
    cursor.execute('''
        ALTER TABLE TopColors
        ADD COLUMN PopularityLevel TEXT
        CHECK (PopularityLevel IN ('High', 'Low', 'Moderate'))
    ''')

    # Step 2: Update the PopularityLevel based on the votes
    cursor.execute('''
        UPDATE TopColors
        SET PopularityLevel = 
            CASE 
                WHEN votes > 20 THEN 'High'
                WHEN votes >= 10 AND votes <= 20 THEN 'Moderate'
                ELSE 'Low'
            END
    ''')

def category_color_purlarity():
    print("==========Q4==========")

    with sqlite3.connect("TopColors.db") as connector: 
         cursor = connector.cursor()
         addAttributeAndRestoreToTable(cursor)
         print("Sucessfully Altear TABLE and restore data ")
         cursor.close()
         connector.commit()

#Q5 

def testSysFunc(): 
    print("==========Q5==========")

  
    with sqlite3.connect("TopColors.db") as connector: 
        cursor = connector.cursor()
        
        # Query 1: Top 3 colors with highest number of votes with their popularity level 
        cursor.execute('''SELECT t.Title, t.Votes, t.PopularityLevel
                        FROM TopColors t 
                        ORDER BY Votes DESC 
                        LIMIT 3''')
        que1 = cursor.fetchall()
        print("Top 3 colors with highest number of votes:")
        if que1:
            print(f"{'Title':<20}{'Votes':<10}{'PopularityLevel':<15}")
            print("-" * 50)
            for row in que1:
                print(f"{row[0]:<20}{row[1]:<10}{row[2]:<15}")
        
        # Query 2: Total number of colors per PopularityLevel
        cursor.execute('''SELECT t.PopularityLevel, COUNT(*) as count 
                         FROM TopColors t 
                         GROUP BY t.PopularityLevel''')
        
        que2 = cursor.fetchall()
        print("\nSummary of the number of colors in each popularity level:")
        if que2: 
            print(f"{'Popularity Level':<20}{'Number of Colors':<15}")
            print("-" * 50)
            for row in que2: 
                print(f"{row[0]:<20}{row[1]:<15}")
        
        cursor.close()
        connector.commit()


def main(): 
    colors = fetch_top_rated_colors()
    data_visualize_color_trend(colors)
    store_top_colors_in_database(colors)
    category_color_purlarity()
    testSysFunc()

   

if __name__ == "__main__":
    main()