import json
import os
import argparse
from datetime import datetime

TRACKER_JSON = "tracker.json"
TRACKER_MD = "PROJECTS_TRACKER.md"

def load_tracker():
    with open(TRACKER_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tracker(data):
    with open(TRACKER_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def generate_markdown(data):
    # Recalculate summary
    total = sum(len(p["projects"]) for p in data["phases"])
    completed = 0
    in_progress = 0
    pending = 0
    
    for phase in data["phases"]:
        for p in phase["projects"]:
            st = p.get("status", "Pending").lower()
            if "complete" in st:
                completed += 1
            elif "progress" in st:
                in_progress += 1
            else:
                pending += 1
                
    pct = round((completed / total) * 100, 1) if total > 0 else 0
    bars = int(pct / 5)
    progress_bar = "█" * bars + "░" * (20 - bars)
    
    data["summary"] = {
        "total_phases": len(data["phases"]),
        "total_projects": total,
        "completed": completed,
        "in_progress": in_progress,
        "pending": pending,
        "completion_rate": f"{pct}%"
    }
    
    md = []
    md.append("# 📊 Machine Learning & Quantitative Trading Project Tracker\n\n")
    md.append("This tracker monitors your progress across all **20 Phases** and **60 Projects** in your syllabus.\n\n")
    md.append("## 📈 Overall Progress Dashboard\n\n")
    md.append("| Metric | Value |\n")
    md.append("| :--- | :--- |\n")
    md.append(f"| **Total Phases** | {len(data['phases'])} |\n")
    md.append(f"| **Total Projects** | {total} (20 General + 40 Quantitative Trading) |\n")
    md.append(f"| **Completed** | **{completed}** 🟢 |\n")
    md.append(f"| **In Progress** | **{in_progress}** 🟡 |\n")
    md.append(f"| **Pending** | **{pending}** ⚪ |\n")
    md.append(f"| **Overall Progress** | `[{progress_bar}] {pct}%` |\n\n")
    md.append("> [!TIP]\n")
    md.append("> Let me know which project you want to start or finish (e.g., *\"Let's work on Phase 1 Project 1\"*). I'll organize your files, build the project modules, and automatically update this tracker.\n\n")
    md.append("## 🗂️ Detailed Project Status Matrix\n\n")

    for phase in data["phases"]:
        md.append(f"### Phase {phase['phase_num']:02d}: {phase['phase_title']}\n")
        md.append(f"📁 Folder: [`{phase['dir']}/`](./{phase['dir']}/)\n\n")
        md.append("| # | Type | Project Title | Folder | Status | Progress | Notes |\n")
        md.append("| :-: | :-- | :--- | :--- | :---: | :---: | :--- |\n")
        for p in phase["projects"]:
            st = p.get("status", "Pending")
            if "Complete" in st:
                badge = "🟢 Completed"
            elif "Progress" in st:
                badge = "🟡 In Progress"
            else:
                badge = "⚪ Pending"
            
            prog = f"{p.get('progress_pct', 0)}%"
            link = f"[`{p['folder']}`](./{p['path']}/)"
            notes = p.get("notes", "") or "-"
            md.append(f"| P{p['project_num']} | `{p['type']}` | **{p['title']}** | {link} | {badge} | `{prog}` | {notes} |\n")
        md.append("\n")

    with open(TRACKER_MD, "w", encoding="utf-8") as f:
        f.writelines(md)

def update_project(phase_num, project_num, status, progress_pct=None, notes=None):
    data = load_tracker()
    found = False
    for phase in data["phases"]:
        if phase["phase_num"] == phase_num:
            for p in phase["projects"]:
                if p["project_num"] == project_num:
                    found = True
                    p["status"] = status
                    if progress_pct is not None:
                        p["progress_pct"] = progress_pct
                    if notes is not None:
                        p["notes"] = notes
                    if "Progress" in status and not p.get("started_at"):
                        p["started_at"] = datetime.now().isoformat()
                    if "Complete" in status:
                        p["completed_at"] = datetime.now().isoformat()
                        p["progress_pct"] = 100
                    break
            if found:
                break
    if not found:
        print(f"Error: Project Phase {phase_num} Project {project_num} not found.")
        return False
    
    save_tracker(data)
    generate_markdown(data)
    print(f"Successfully updated Phase {phase_num} Project {project_num} to '{status}'.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update ML Project Tracker")
    parser.add_argument("--phase", type=int, help="Phase number (1-20)")
    parser.add_argument("--project", type=int, help="Project number (1-3)")
    parser.add_argument("--status", type=str, choices=["Pending", "In Progress", "Completed"], help="Status")
    parser.add_argument("--progress", type=int, help="Progress percentage (0-100)")
    parser.add_argument("--notes", type=str, help="Notes or comments")
    parser.add_argument("--refresh", action="store_true", help="Regenerate Markdown from JSON")
    
    args = parser.parse_args()
    if args.refresh:
        data = load_tracker()
        generate_markdown(data)
        print("Regenerated tracker markdown.")
    elif args.phase and args.project and args.status:
        update_project(args.phase, args.project, args.status, args.progress, args.notes)
    else:
        parser.print_help()
