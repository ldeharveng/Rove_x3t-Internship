# HUVTSP Rove_x3t Internship Project - Flight Data Collector

A Python script that collects flight data using the Amadeus API for multiple travel routes and stores the data in a CSV file. Optionally, you can export the CSV data to a local SQLite database.

## Features

- ✈️ Connects to Amadeus API to fetch real-time flight data
- 🗺️ Pre-configured with multiple international travel routes
- 📊 Collects comprehensive flight information (prices, airlines, times, dates)
- 💾 Stores data in a CSV file (no SQL by default)
- 🗄️ Optionally exports CSV data to SQLite database (`database.db`)
- 📈 Provides data analysis and statistics
- 🔄 Automatic rate limiting to respect API limits

## Travel Routes

The script collects data for these routes:
1. **Madrid to Barcelona** (MAD → BCN)
2. **New York to Los Angeles** (JFK → LAX)
3. **Berlin to Paris** (BER → PAR)
4. **London to San Francisco** (LON → SFO)

## Date Range

- The script collects flight data for **2025-08-01** through **2025-08-04** for each route.

## Data

- **On a testing environment, all retrieved data is not real. If real data is needed, applying for the production environment in Amadeus is necessary.**

## Setup Instructions

### 1. Get Amadeus API Credentials
1. Visit [Amadeus for Developers](https://developers.amadeus.com/)
2. Create a free account
3. Create a new application to get your API Key and Secret

### 2. Set Up Environment Variables
Create a `.env` file in the project root with your credentials:
```
AMADEUS_API_KEY=your_amadeus_api_key_here
AMADEUS_API_SECRET=your_amadeus_api_secret_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Script
```bash
python main.py
```

## What the Script Does

1. **Initialization**: Connects to Amadeus API
2. **Data Collection**: For each route, searches flights for 2025-08-01 to 2025-08-04
3. **Data Storage**: Saves flight details to a CSV file (`flight_data_export.csv`)
4. **Analysis**: Provides statistics about collected data
5. **Optional SQL Export**: Converts the CSV file to a SQLite database (`database.db`)

## Output Files

- `flight_data_export.csv` - CSV export of all data
- `database.db` - SQLite database (if you choose to export)
- `flight_data_collection.log` - Detailed execution log

## Optional: Export CSV to SQLite

After the CSV is generated, the script will automatically convert it to a SQLite database (`database.db`) with a table named `flight_data_sql`.

## Example Output

```
=== FLIGHT DATA STATISTICS ===
Total flights collected: 12

=== FLIGHTS BY ROUTE ===
                        price_amount                
route_name             currency    count  min    max    mean                
Madrid to Barcelona      EUR         3    45.0   90.0   60.00
New York to Los Angeles  USD         4    120.0  350.0  200.00
...

=== TOP AIRLINES BY FLIGHT COUNT ===
            price_amount         
airline_name          count    mean       
Delta Air Lines         4     210.00
American Airlines       3     180.00
...
```

## Troubleshooting

- **API Errors**: Check your credentials in `.env` file
- **Sandbox Limitations**: The Amadeus sandbox only supports a limited set of routes and dates. If you get a 400 error, try a different route or date.
- **Network Issues**: Script includes retry logic for temporary failures
- **Missing Dependencies**: Run `pip install -r requirements.txt`

## Notes

- Data collection is limited by the Amadeus sandbox environment for free accounts
- **On a testing environment, all retrieved data is not real. If real data is needed, applying for the production environment in Amadeus is necessary.**
- The script is designed to be run multiple times safely (prevents duplicates in the CSV/SQL)
- All times are in UTC as provided by Amadeus API
- The code is now clean, efficient, and free of comments for maximum clarity and performance



Algorithm.py
Input

Your Rove miles balance
Flight search (origin, destination, date)

Output

Best redemption option (highest cents-per-mile value)
Top 3 recommendations
Analysis summary
