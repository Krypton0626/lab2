import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Store labeled data with all necessary information
labeled_data = {}

def submit_label(label, index, label_status, annotation, sampling_method):
    """Store the labeled data with all necessary information."""
    row_id = f"{sampling_method}_{index}"  # Create unique identifier
    labeled_data[row_id] = {
        'index': index,
        'label': label,
        'annotation': annotation,
        'sampling_method': sampling_method
    }
    label_status.config(text=f"Current Label: {label}")

def save_annotations():
    """Save the labeled data to CSV with proper organization."""
    if not labeled_data:
        messagebox.showwarning("No Data", "No data has been labeled yet!")
        return

    # Group data by sampling method
    method_groups = {}
    for row_id, data in labeled_data.items():
        method = data['sampling_method']
        if method not in method_groups:
            method_groups[method] = []
        method_groups[method].append(data)

    # Create organized data list
    data_list = []
    for method in sorted(method_groups.keys()):
        # Add method header
        data_list.append({
            'Index': f"=== {method} ===",
            'Label': "",
            'Annotation': "",
            'Sampling_Method': method
        })
        
        # Add data rows for this method
        method_data = sorted(method_groups[method], key=lambda x: x['index'])
        for item in method_data:
            data_list.append({
                'Index': item['index'],
                'Label': item['label'],
                'Annotation': item['annotation'],
                'Sampling_Method': item['sampling_method']
            })
        
        # Add separator
        data_list.append({
            'Index': "",
            'Label': "",
            'Annotation': "",
            'Sampling_Method': ""
        })

    # Save to CSV
    df = pd.DataFrame(data_list)
    df.to_csv('labeled_data.csv', index=False)
    messagebox.showinfo("Success", "Labels saved successfully to 'labeled_data.csv'")

def show_labeled_data():
    """Display the current labeled data."""
    custom_window = tk.Toplevel()
    custom_window.title("Labeled Data")
    
    text_widget = tk.Text(custom_window, wrap=tk.WORD, width=60, height=20)
    text_widget.pack(padx=10, pady=10)
    
    # Group by sampling method
    method_groups = {}
    for row_id, data in labeled_data.items():
        method = data['sampling_method']
        if method not in method_groups:
            method_groups[method] = []
        method_groups[method].append(data)
    
    # Display organized data
    for method in sorted(method_groups.keys()):
        text_widget.insert(tk.END, f"\n=== {method} ===\n\n")
        method_data = sorted(method_groups[method], key=lambda x: x['index'])
        for item in method_data:
            text_widget.insert(tk.END, 
                f"Row {item['index']}: {item['label']} - {item['annotation']}\n")
    
    text_widget.config(state=tk.DISABLED)
    close_button = tk.Button(custom_window, text="Close", command=custom_window.destroy)
    close_button.pack(pady=5)

def finish_labeling(root):
    save_annotations()
    show_labeled_data()
    root.destroy()

def load_batch(method, tab_info):
    current_index = tab_info['current_index']
    data = tab_info['data']
    frame = tab_info['scrollable_frame']
    
    # Clear existing widgets
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Load the batch of rows
    for i in range(current_index, min(current_index + 5, len(data))):
        row = data.iloc[i]
        label_text = f"Ride from {row['source']} to {row['destination']}, Price: {row['price']}"
        
        label_frame = ttk.Frame(frame)
        label_frame.pack(pady=5, fill="x", padx=5)
        
        ttk.Label(label_frame, text=label_text).pack(side="left")
        
        label_status = ttk.Label(label_frame, text="Not labeled yet", width=15)
        label_status.pack(side="left", padx=5)
        
        ttk.Button(
            label_frame,
            text="Valid",
            command=lambda i=row.name, ls=label_status, ann=label_text, sm=method:
                submit_label("Valid", i, ls, ann, sm)
        ).pack(side="left", padx=5)
        
        ttk.Button(
            label_frame,
            text="Invalid",
            command=lambda i=row.name, ls=label_status, ann=label_text, sm=method:
                submit_label("Invalid", i, ls, ann, sm)
        ).pack(side="left", padx=5)
    
    tab_info['current_index'] = current_index + 5

def labeling_tool(sampling_results):
    try:
        root = tk.Tk()
        root.title("Manual Labeling Tool")
        
        # Create notebook for tabs
        notebook = ttk.Notebook(root)
        notebook.pack(padx=10, pady=5, expand=True, fill="both")
        
        # Create separate tabs for each sampling method
        sampling_methods = sampling_results['sampling_method'].unique()
        tabs = {}
        
        for method in sampling_methods:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=method)
            
            canvas = tk.Canvas(tab)
            scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            scrollbar.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)
            
            tabs[method] = {
                'frame': tab,
                'current_index': 0,
                'data': sampling_results[sampling_results['sampling_method'] == method].reset_index(),
                'scrollable_frame': scrollable_frame
            }
            
            load_batch(method, tabs[method])
        
        # Add buttons at the bottom
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=5)
        
        ttk.Button(
            button_frame,
            text="Next Batch",
            command=lambda: load_batch(
                notebook.tab(notebook.select(), "text"),
                tabs[notebook.tab(notebook.select(), "text")]
            )
        ).pack(side="left", padx=5)
        
        ttk.Button(
            button_frame,
            text="Finish",
            command=lambda: finish_labeling(root)
        ).pack(side="left", padx=5)
        
        root.mainloop()
    except Exception as e:
        print(f"An error occurred in labeling_tool: {e}")
