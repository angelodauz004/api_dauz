import requests

API_KEY = "h523hDtETbkJ3nSJL323hjYLXbCyDaRZ"
BASE_URL = "https://api.recruitment.shq.nz"

def get_domains(client_id):
    url = f"{BASE_URL}/domains/{client_id}?api_key={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Domains Response:", data)  # Print response data for debugging
    return data

def get_dns_records(zone_id):
    if not zone_id:
        print("No zone ID provided.")
        return []
    
    url = f"{BASE_URL}/zones/{zone_id}?api_key={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("DNS Records Response:", data)  # Print response data for debugging
    return data

def main():
    client_id = 100
    domains = get_domains(client_id)
    print("Domains and DNS Records for client_id 100:")
    
    for domain in domains:  # Iterate directly over the list
        print(f"Domain: {domain['name']}")
        for zone in domain['zones']:
            zone_id = zone['uri'].split('/')[-1]  # Extract the zone ID from the URI
            print(f"  Zone: {zone_id}")
            dns_records = get_dns_records(zone_id)
            for record in dns_records:
                print(f"    Record: {record['type']} {record['name']} -> {record['value']}")

if __name__ == "__main__":
    main()