# ==================================================
# RSB SIMULATION AGENT - PORTFOLIO CLIENT
# Forwards simulated security vectors to RSB Cloud
# ==================================================

import urllib.request
import json
import sys

# CHANGE THIS TO YOUR ACTUAL RENDER LIVE URL
CLOUD_ENDPOINT = "https://codigo-na-nuvem.lovable.app/api/v1/threat
TEST_API_KEY = "raven_test_key_abc123"

def send_payload(event_type, description):
    print(f"\n🛰 Formatting security packet [{event_type}]...")
    
    payload = {
        "tipo_evento": event_type,
        "endereco_ip": "198.51.100.77",
        "descricao": description
    }
    
    data = json.dumps(payload).encode('utf-8')
    
    req = urllib.request.Request(CLOUD_ENDPOINT, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-RSB-Key", TEST_API_KEY)
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("✅ [RSB GATEWAY RESPONSE]: Status 200 - Packet Processed Successfully.")
                print("💻 Check your live web dashboard to view the telemetry change!")
            else:
                print(f"⚠ Unexpected Status Code: {response.status}")
    except Exception as e:
        print(f"❌ Connection Architecture Failure: {str(e)}")

def main():
    print("=" * 60)
    print("🦅 RAVEN SECURE BUILDS - EDGE SIMULATION ENGINE")
    print("=" * 60)
    print("Select a threat payload vectors to fire against cloud node:")
    print("1. Path Traversal Simulation (../etc/passwd)")
    print("2. SQL Injection Payload (UNION SELECT * FROM corporate_vault)")
    print("3. Cross-Site Scripting String (<script>malicious_payload()</script>)")
    print("4. Trigger Brute Force Scenario (Multiple Failed Logins)")
    print("5. Exit Client")
    
    choice = input("\nEnter choice vector [1-5]: ")
    
    if choice == "1":
        send_payload("path_traversal", "Attempting directory escape bypass vector: ../../etc/passwd")
    elif choice == "2":
        send_payload("sql_injection", "Malicious target query injection executed: ' UNION SELECT null, password FROM users --")
    elif choice == "3":
        send_payload("xss_attack", "Injecting persistent interface exploit layout context: <script>document.cookie()</script>")
    elif choice == "4":
        print("\n🔥 Firing rapid brute-force sequence packet series...")
        for i in range(5):
            send_payload("login_falhou", f"Unauthorized access authentication interface failure attempt #{i+1}")
    else:
        print("Exiting node execution pipeline.")
        sys.exit()

if __name__ == "__main__":
    while True:
        main()
