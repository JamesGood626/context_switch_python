import os
import subprocess
import webbrowser
from paths import PREVIEW_EXE_PATH
from contexts import context_dict


def open_ebooks(paths):
    subprocess.Popen([PREVIEW_EXE_PATH, *paths])


def open_project_in_vscode(path):
    os.system("code " + path)


def loop_and_open_projects(projects):
    for project in projects:
        open_project_in_vscode(project)


def open_new_browser_tab(url):
    webbrowser.open_new_tab(url)


def loop_and_open_tabs(urls):
    for url in urls:
        open_new_browser_tab(url)


def handle_opening_contexts(context):
    ebooks_len = len(context["ebooks"])
    urls_len = len(context["urls"])
    projects_len = len(context["projects"])
    if ebooks_len > 0:
        open_ebooks(context["ebooks"])
    if urls_len > 0:
        loop_and_open_tabs(context["urls"])
    if projects_len > 0:
        loop_and_open_projects(context["projects"])


def open_contexts(args):
    invalid_key_supplied = False
    for key in args:
        if key in context_dict.keys():
            handle_opening_contexts(context_dict[key])
        else:
            invalid_key_supplied = True
            break
    if invalid_key_supplied:
        log_err_feedback('Incorrect context keys')


def log_err_feedback(msg):
    print(msg)
