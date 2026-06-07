import csv
import time
from pathlib import Path

def print_banner():
    print("=" * 60)
    print("        🚀 COLD REACH SaaS EMAIL ENGINE v1.0.0 🚀        ")
    print("             Automate Value. Scale Outreach.            ")
    print("=" * 60)

def main():
    print_banner()
    
    script_dir = Path(__file__).parent.resolve()
    template_path = script_dir / "template.txt"
    csv_path = script_dir / "prospects.csv"
    
    
    if not template_path.exists() or not csv_path.exists():
        print("❌ Error: Missing 'template.txt' or 'prospects.csv' in this folder.")
        return

    print("🔄 Initializing generation pipeline...")
    time.sleep(0.8) 
    
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f)) 
        total_records = len(reader)
        
        print(f"📈 Found {total_records} prospects in queue.\n")
        print("⚡ Processing Batch:")
        print("-" * 40)
        
        count = 0
        for row in reader:
            personalized_email = template_content.format(
                name=row['name'].strip(),
                company=row['company'].strip(),
                pain_point=row['pain_point'].strip(),
                product_name=row['product_name'].strip()
            )
            
            
            safe_name = row['name'].strip().replace(" ", "_")
            file_name = f"out_{safe_name}.txt"
            (script_dir / file_name).write_text(personalized_email, encoding="utf-8")
            
            
            time.sleep(0.4) 
            print(f"  [SUCCESS] -> Generated outreach for {row['name']} ({row['company']})")
            count += 1
            
    print("-" * 40)
    print(f"🎉 Success! {count}/{total_records} personalized emails deployed.")
    print("=" * 60)

if __name__ == "__main__":
    main()
