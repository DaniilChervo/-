import shutil, os, glob, sys

print(f"Python version: {sys.version}")

src_dir = r"C:\Users\theda\.gemini\antigravity-ide\brain\f4a7548e-e8bc-43fb-8498-0d3fdd2d5d47"
dst_dir = r"C:\Users\theda\OneDrive\Рабочий стол\site-for-bitrix\images"

print(f"Source dir exists: {os.path.exists(src_dir)}")
print(f"Source dir accessible: ", end="")
try:
    files = os.listdir(src_dir)
    print(f"YES — {len(files)} files found")
    for f in files:
        if f.endswith(".png"):
            print(f"  PNG: {f}")
except Exception as e:
    print(f"NO — {e}")

print(f"\nDest dir: {dst_dir}")
os.makedirs(dst_dir, exist_ok=True)

mapping = {
    "icon_funnel": "icon_funnel.png",
    "icon_analytics": "icon_analytics.png",
    "icon_automation": "icon_automation.png",
    "icon_integration": "icon_integration.png",
    "bitrix_ecosystem": "bitrix_ecosystem.png",
    "crm_dashboard": "crm_dashboard.png",
    "icon_telegram": "icon_telegram.png",
    "icon_whatsapp": "icon_whatsapp.png",
}

for prefix, dst_name in mapping.items():
    pattern = os.path.join(src_dir, f"{prefix}_*.png")
    matches = glob.glob(pattern)
    if matches:
        src = matches[0]
        dst = os.path.join(dst_dir, dst_name)
        shutil.copy2(src, dst)
        print(f"Copied: {os.path.basename(src)} -> {dst_name}")
    else:
        print(f"NOT FOUND: {prefix} (pattern: {pattern})")
        
print("\nDone!")
