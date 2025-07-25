# HUVTSP ROVER - Flight Data Collector

A Python script that collects flight data using the Amadeus API for multiple travel routes and stores the data in a SQLite database.

## Features

- ✈️ Connects to Amadeus API to fetch real-time flight data
- 🗺️ Pre-configured with 6 international travel routes
- 📊 Collects comprehensive flight information (prices, airlines, times, dates)
- 💾 Stores data in SQLite database with duplicate prevention
- 📈 Provides data analysis and statistics
- 📋 Exports data to CSV for further analysis
- 🔄 Automatic rate limiting to respect API limits
- 📝 Comprehensive logging

## Travel Routes

The script collects data for these routes:
1. **NYC to Shanghai** (JFK → PVG)
2. **Hong Kong to Taipei** (HKG → TPE)
3. **Praia to Recife** (RAI → REC)
4. **Paris to Tokyo** (CDG → HND)
5. **Toronto to Seattle** (YYZ → SEA)
6. **Los Angeles to Chicago** (LAX → ORD)

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

1. **Initialization**: Connects to Amadeus API and sets up SQLite database
2. **Data Collection**: For each route, searches flights for 30 consecutive days
3. **Data Storage**: Saves flight details to SQLite database
4. **Analysis**: Provides statistics about collected data
5. **Export**: Creates CSV file with all collected data

## Collected Data Points

For each flight, the script collects:
- Route information (origin, destination, route name)
- Flight timing (departure/arrival dates and times)
- Airline details (code, name, flight number)
- Pricing (amount and currency)
- Aircraft information
- Flight characteristics (duration, stops, booking class)
- Availability (seats available)
- Collection timestamp

## Database Schema

The SQLite database includes a `flights` table with:
- Unique constraints to prevent duplicates
- Indexed fields for efficient querying
- Comprehensive flight information storage

## Output Files

- `flight_data.db` - SQLite database with all flight data
- `flight_data_export.csv` - CSV export of all data
- `flight_data_collection.log` - Detailed execution log

## Rate Limiting

The script includes automatic rate limiting:
- 1-second delay between individual API calls
- 2-second delay between different routes
- Respects Amadeus API guidelines

## Error Handling

- Comprehensive error logging
- Graceful handling of API errors
- Duplicate data prevention
- Network timeout protection

## Usage Tips

1. **First Run**: Start with a small date range to test your API credentials
2. **API Limits**: Free Amadeus accounts have monthly quotas - monitor your usage
3. **Data Analysis**: Use the built-in statistics or export to CSV for external analysis
4. **Scheduling**: Consider running the script daily to build a comprehensive dataset

## Example Output

```
=== FLIGHT DATA STATISTICS ===
Total flights collected: 1,247

=== FLIGHTS BY ROUTE ===
route_name              flight_count  min_price  max_price  avg_price  price_currency
NYC to Shanghai         234          456.78     2134.56    987.45     USD
Hong Kong to Taipei     198          123.45     567.89     234.56     USD
...

=== TOP AIRLINES BY FLIGHT COUNT ===
airline_name           flight_count  avg_price
Delta Air Lines        145          789.23
United Airlines        132          856.78
...
```

## Troubleshooting

- **API Errors**: Check your credentials in `.env` file
- **Network Issues**: Script includes retry logic for temporary failures
- **Database Errors**: Delete `flight_data.db` to reset database
- **Missing Dependencies**: Run `pip install -r requirements.txt`

## Notes

- Data collection for 30 days across 6 routes may take 3-6 minutes
- Free Amadeus API accounts have usage limits
- Script is designed to be run multiple times safely (prevents duplicates)
- All times are in UTC as provided by Amadeus API 