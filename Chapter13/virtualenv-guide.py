#* ========================================================
#* PYTHON VIRTUAL ENVIRONMENT: COMPLETE A TO Z GUIDE
#* ========================================================

#* This file does not execute like a normal script — 
#* It’s a step-by-step instruction guide with commands explained.
#* Follow each step in your terminal or VS Code terminal.

#* -----------------------------
#* 1️⃣ CHECK PYTHON VERSION
#* -----------------------------
#* Open your terminal and run:
#^ python --version

#* Make sure you have Python 3.6+ installed.

#* -----------------------------
#* 2️⃣ CREATE PROJECT FOLDER
#* -----------------------------
#* In terminal:
#^ mkdir my_project
#^ cd my_project

#* -----------------------------
#* 3️⃣ CREATE VIRTUAL ENVIRONMENT
#* -----------------------------
#* Run:
#^ python -m venv my-env

#* This creates a folder named `my-env` with:
#* - Scripts (Windows) or bin (Linux/Mac)
#* - Python executable
#* - Local site-packages (installed libraries)

#* -----------------------------
#* 4️⃣ ACTIVATE VIRTUAL ENVIRONMENT
#* -----------------------------
#* Windows:
#^ my-env\Scripts\activate

#* Mac / Linux:
#^ source my-env/bin/activate

#* If successful, your terminal will show:
#^ (my-env) ➜

#* -----------------------------
#* 5️⃣ INSTALL PACKAGES
#* -----------------------------
#* For example, install requests and flask:
#^ pip install requests flask

#* Verify installed packages:
#^ pip list

#* -----------------------------
#* 6️⃣ SAVE INSTALLED PACKAGES
#* -----------------------------
#* To share with others:
#^ pip freeze > requirements.txt

#* This file lists all packages + versions.

#* -----------------------------
#* 7️⃣ INSTALL FROM requirements.txt
#* -----------------------------
#* Anyone can recreate your environment:
#^ pip install -r requirements.txt

#* -----------------------------
#* 8️⃣ DEACTIVATE VIRTUAL ENVIRONMENT
#* -----------------------------
#* When done working:
#^ deactivate

#* This brings you back to your global Python.

#* -----------------------------
#* 9️⃣ DELETE A VIRTUAL ENVIRONMENT
#* -----------------------------
#* Just delete the folder:
#^ rm -rf my-env

#* -----------------------------
#* 1️⃣0️⃣ EXTRA: BEST PRACTICES
#* -----------------------------
#* #! Always use one virtual env per project.
#* #! Never push the `my-env` folder to Git.
#* #! Add it to .gitignore.
#* #! Always share requirements.txt.

#* -----------------------------
#* 1️⃣1️⃣ CHECK PYTHON PATH
#* -----------------------------
#* Confirm your venv is active:
#^ which python  # Mac/Linux
#^ where python  # Windows

#* It should show path inside your my-env folder.

#* -----------------------------
#* 1️⃣2️⃣ BONUS: VENV USING virtualenv
#* -----------------------------
#* Install virtualenv if needed:
#^ pip install virtualenv

#* Create:
#^ virtualenv my-env

#* Activate same as above.

#* -----------------------------
#* ✅ YOU DID IT!
#* -----------------------------
#* You now know how to:
#* - Create
#* - Activate
#* - Install packages
#* - Freeze requirements
#* - Recreate environments
#* - Deactivate & clean up

#* -----------------------------
#* 📌 END OF GUIDE
#* -----------------------------
