# 🌱 Smart Weather Advisory System

## 📌 Problem Statement  
Agriculture in South Africa is highly vulnerable to climate change. Farmers face unpredictable weather patterns such as sudden rainfall, droughts, frost, and heatwaves, which directly affect crop yields and income. Without localized and timely weather information, they risk planting unsuitable crops, wasting resources, and suffering economic losses.

### ✅ Our Solution  
We developed a **Smart Weather Advisory System**, a web-based agricultural decision-support platform that empowers farmers with:  
- 🌦 **Real-time weather forecasts** (via OpenWeatherMap API)  
- 🌱 **Crop recommendations** (based on soil, weather, and region)  
- 📅 **Smart planting calendars**  
- 🐛 **Pest & disease database** with prevention strategies  
- 🤖 **AI-powered chatbot** for instant farming guidance  
- 📓 **Garden Journal** for tracking farm activities  

---

## 🏗 System Design  
Our system follows a **3-Tier Architecture**:  

- **Client Tier**: Web browser (HTML, CSS, JS, Bootstrap, Chart.js)  
- **Application Tier**: Django Web Server with services for authentication, weather, crop recommendation, pest database, chatbot integration, and APIs  
- **Data Tier**: SQLite Database + External APIs (OpenWeatherMap, LANDBOT)  

### 🔗 API Endpoints  
- `/api/weather/<location>/` → Fetch weather data  
- `/api/crop/recommend/` → Get crop recommendations  
- `/api/pests/<crop>/` → Pest information  
- `/api/chatbot/query/` → Chatbot queries  
- `/api/journal/entries/` → Retrieve journal entries  

---

## 🎨 Features & Demo  

### GUI Pages  
- **Home Page** → Overview + Mission  
- **Selection Page** → User inputs preferences  
- **Weather Dashboard** → 7-day trends, temperature, pest analysis  
- **Smart Planting Calendar** → Suggests optimal planting times  
- **Pest Database** → Info on pests & prevention  
- **Garden Journal** → Record activities & photos  
- **AI Chatbot** → Farmwise Assistant for guidance  

### 📊 Example Visualizations  
- Temperature trend line chart  
- Pest distribution pie chart  
- Unit test performance bar chart  

---

## ⚙️ Setup & Tools  
**Backend**: Python (3.10+), Django (4.2+), Django REST Framework  
**Frontend**: HTML5, CSS3, JavaScript (ES6+), Bootstrap, Chart.js  
**Database**: SQLite (default for dev)  
**APIs**: OpenWeatherMap, LANDBOT  
**Dev Tools**: VS Code, Git, GitHub  

### 🚀 Installation  
```bash
# Clone repo
git clone https://github.com/your-username/SmartWeatherAdvisorySystem.git
cd SmartWeatherAdvisorySystem

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
```

---

## 👥 Team Members  
- Nkoana Hope Lerato – 202204804  
- Mawela Mpho Precious – 202233722  
- Khalo Ayanda Girly – 202213324  
- Dlamini Kelebogile Sylvia – 202224253  

---

## 📌 References  
- Olabanji, Ndarana & Davis (2021) – *Impact of Climate Change on Crop Production in South Africa*  
- Kephe, Ayisi & Petja (2021) – *Challenges & Opportunities in Crop Simulation Modelling*  
- FAO (2019) – *Climate-Smart Agriculture Sourcebook*  
