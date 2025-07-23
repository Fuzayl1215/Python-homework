import pandas as pd
import sqlite3

# Connect to chinook.db
conn = sqlite3.connect('chinook.db')

print(conn)


# Load Invoices and Customers tables
invoices = pd.read_sql_query("SELECT * FROM Invoice", conn)
customers = pd.read_sql_query("SELECT * FROM Customer", conn)

# Total amount spent per customer
total_spent = invoices.groupby('CustomerId')['Total'].sum().reset_index(name='TotalSpent')

# Merge with customer info
customer_spending = pd.merge(total_spent, customers, on='CustomerId')

# Get top 5 customers by amount spent
top5_customers = customer_spending.sort_values('TotalSpent', ascending=False).head(5)

# Select and display relevant columns
result_top5 = top5_customers[['CustomerId', 'FirstName', 'LastName', 'TotalSpent']]
print(result_top5)

invoice_items = pd.read_sql_query("SELECT * FROM InvoiceLine", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)
albums = pd.read_sql_query("SELECT AlbumId FROM Album", conn)


# Merge invoice items with tracks to know which album each track belongs to
merged = invoice_items.merge(tracks, on='TrackId', how='left')

# Group by CustomerId and AlbumId → get how many tracks each customer bought per album
customer_album_purchases = merged.groupby(['InvoiceId', 'CustomerId', 'AlbumId'])['TrackId'].nunique().reset_index(name='TracksPurchased')

# Get total tracks in each album
album_track_counts = tracks.groupby('AlbumId')['TrackId'].nunique().reset_index(name='TotalTracksInAlbum')

# Merge to compare tracks purchased vs. total tracks in album
comparison = customer_album_purchases.merge(album_track_counts, on='AlbumId')

# Determine whether full album was bought
comparison['BoughtFullAlbum'] = comparison['TracksPurchased'] == comparison['TotalTracksInAlbum']

# If a customer bought at least one full album → full album buyer
customer_pref = comparison.groupby('CustomerId')['BoughtFullAlbum'].any().reset_index()
customer_pref['Preference'] = customer_pref['BoughtFullAlbum'].apply(lambda x: 'Full Album' if x else 'Individual Tracks')

# Percentage summary
preference_summary = customer_pref['Preference'].value_counts(normalize=True) * 100
print(preference_summary)
