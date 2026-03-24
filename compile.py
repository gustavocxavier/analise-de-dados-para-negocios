import os
import subprocess
import argparse
from pathlib import Path

def setup_jupyter_book_config(course_dir, course_name):
    """Creates minimal _config.yml and _toc.yml required by Jupyter Book."""
    config_path = os.path.join(course_dir, '_config.yml')
    toc_path = os.path.join(course_dir, '_toc.yml')
    
    # Write minimal config
    if not os.path.exists(config_path):
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(f"title: {course_name}\nlogo: ''\nexecute:\n  execute_notebooks: off\n")
            
    # Write minimal Table of Contents (aggregating all notebooks)
    if not os.path.exists(toc_path):
        notebooks = [nb for nb in Path(course_dir).rglob('*.ipynb') 
                     if '.ipynb_checkpoints' not in str(nb) and '_build' not in str(nb)]
        notebooks.sort()
        
        with open(toc_path, 'w', encoding='utf-8') as f:
            f.write("format: jb-book\nroot: README\nchapters:\n")
            for nb in notebooks:
                # Jupyter book expects forward slashes and no .ipynb extension
                rel_path = nb.relative_to(course_dir).with_suffix('').as_posix()
                f.write(f"  - file: {rel_path}\n")
                
    # Create a dummy README.md for the root if it doesn't exist
    readme_path = os.path.join(course_dir, 'README.md')
    if not os.path.exists(readme_path):
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(f"# {course_name}\n\nWelcome to the course webbook.")

def compile_webbook(course_dir):
    """Builds the HTML webbook using jupyter-book."""
    print(f"📚 Building Jupyter Book for '{course_dir}'...")
    try:
        subprocess.run(["jupyter-book", "build", course_dir], check=True)
        print("✅ Webbook built successfully! Find it in _build/html/")
    except subprocess.CalledProcessError:
        print("❌ Error: Ensure 'jupyter-book' is installed (pip install jupyter-book).")

def compile_slides(course_dir):
    """Converts all notebooks into Reveal.js HTML slides."""
    print(f"📽️ Compiling Reveal.js slides...")
    notebooks = Path(course_dir).rglob('*.ipynb')
    
    for path in notebooks:
        if '.ipynb_checkpoints' in str(path) or '_build' in str(path):
            continue
        print(f"  Converting {path.name} to slides...")
        try:
            subprocess.run(["jupyter", "nbconvert", "--to", "slides", str(path)], check=True)
        except subprocess.CalledProcessError:
             print(f"❌ Error converting {path.name}.")
             
    print("✅ All slides compiled successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deterministic Course Compiler Script")
    parser.add_argument("--course_dir", required=True, help="Directory of the generated course")
    parser.add_argument("--course_name", required=True, help="Display title of the course")
    
    args = parser.parse_args()
    
    print("🚀 Starting compilation process...")
    setup_jupyter_book_config(args.course_dir, args.course_name)
    compile_slides(args.course_dir)
    compile_webbook(args.course_dir)