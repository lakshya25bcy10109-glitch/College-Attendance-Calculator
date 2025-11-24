import sys
import math

class SubjectAttendance:
    def __init__(self, subject_name, attended_classes=0, total_classes=0):  
        self.subject_name = subject_name
        self.attended_classes = attended_classes
        self.total_classes = total_classes
        self.percentage = 0.0
        self._update_values(attended_classes, total_classes)

    def _update_values(self, attended, total):
        if attended < 0 or total < 0:
            raise ValueError("Class counts cannot be negative.")
        if total < attended:
            raise ValueError("Total classes cannot be less than attended classes.")
            
        self.attended_classes = attended
        self.total_classes = total
        self._calc_percentage()

    def update_attendance(self, attended, total):
        self._update_values(attended, total)

    def _calc_percentage(self):
        if self.total_classes > 0:
            self.percentage = (self.attended_classes / self.total_classes) * 100.0
        else:
            self.percentage = 0.0
        return self.percentage

    def get_status(self):
        pct = self.percentage
        
        if pct < 75.0:
            return "At Risk - Below 75%"
        elif pct < 90.0:
            return "Good"
        elif pct < 96.0:
            return "Excellent"
        else:
            return "Outstanding"

    def calculate_classes_needed(self, target=75.0):
        if self.percentage >= target:
            return 0
            
        if target >= 100:
            return -1
        
      
        num = (target * self.total_classes) - (100 * self.attended_classes)
        denom = 100 - target
        
        if denom == 0:
            return -1
            
        classes_needed = num / denom
        return math.ceil(classes_needed) if classes_needed > 0 else 0

    def calculate_skippable_classes(self, target=75.0):
        if self.percentage < target:
            return 0
            
        if target <= 0:
            return 999
            
       
        max_total = (100 * self.attended_classes) / target
        skippable = max_total - self.total_classes
        return int(skippable) if skippable > 0 else 0
        
    def show_report(self):
        print("-" * 50)
        print(f"Subject: {self.subject_name}")
        print(f"Attended: {self.attended_classes} / {self.total_classes}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Status: {self.get_status()}")
        
       
        MIN_ATTENDANCE = 75.0
        
        if self.percentage < MIN_ATTENDANCE:
            needed = self.calculate_classes_needed(MIN_ATTENDANCE)
            if needed > 0:
                print(f"Action Required: Attend next {needed} classes to reach {MIN_ATTENDANCE:.0f}%")
        else:
            skip = self.calculate_skippable_classes(MIN_ATTENDANCE)
            if skip > 0:
                print(f"Buffer: Can skip {skip} more classes while staying above {MIN_ATTENDANCE:.0f}%")
        
        print("-" * 50)


class AttendanceTracker:
    def __init__(self): 
        self.subjects = {}
    
    def add_subject(self, name, attended, total):
        try:
            if name in self.subjects:
                self.subjects[name].update_attendance(attended, total)
                return True
            else:
               
                self.subjects[name] = SubjectAttendance(name, attended, total) 
                return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def get_overall_attendance(self):
        if not self.subjects:
            return 0.0
        
        total_att = sum(s.attended_classes for s in self.subjects.values())
        total_cls = sum(s.total_classes for s in self.subjects.values())
        
        if total_cls == 0:
            return 0.0
        return (total_att / total_cls) * 100.0
    
    def show_all_reports(self):
        if not self.subjects:
            print("\nNo subjects added yet.")
            return
        
        print("\n" + "=" * 50)
        print("ATTENDANCE     REPORT".center(50))
        print("=" * 50)
        
        for subject in self.subjects.values():
            subject.show_report()
        
        overall = self.get_overall_attendance()
        print("\n" + "=" * 50)
        print(f"Overall Attendance: {overall:.2f}%")
        
        if overall < 75.0:
            print("WARNING: Overall attendance is below minimum requirement!")
        elif overall >= 90.0:
            print("Excellent! Keep up the good work!")
        print("=" * 50)


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("\n" + "=" * 50)
    print("College Attendance Tracker".center(50))
    print("=" * 50)
    print("Minimum attendance requirement is: 75%\n")
    
  
    tracker = AttendanceTracker() 

    while True:
        print("\n      Options:")
        print("1. Add/Update Subject")
        print("2. View Full Report")
        print("3. View Single Subject")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()

        if choice == '1':
            name = input("Subject name: ").strip()
            
            if not name:
                print("Subject name cannot be empty.")
                continue
            
            attended = get_integer_input(f"Classes attended for {name}: ")
            total = get_integer_input(f"Total classes for {name}: ")
            
            if tracker.add_subject(name, attended, total):
                print(f"\n'{name}' updated successfully!")
                tracker.subjects[name].show_report()

        elif choice == '2':
            tracker.show_all_reports()

        elif choice == '3':
            if not tracker.subjects:
                print("\nNo subjects available.")
                continue
            
            print("\nAvailable subjects:", ", ".join(tracker.subjects.keys()))
            name = input("Enter subject name: ").strip()
            
            if name in tracker.subjects:
                tracker.subjects[name].show_report()
            else:
                print(f"Subject '{name}' not found.")

        elif choice == '4':
            print("\n        Exiting. Good luck with your studies!")
            sys.exit(0)

        else:
            print("Invalid choice. Please select from the numbers 1-4.")


if __name__ == "__main__": 
    main()