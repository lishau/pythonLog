<!doctype html><html lang="en"><head><meta charset="utf-8"><title>JupyterLab</title><meta name="viewport" content="width=device-width,initial-scale=1">   <script id="jupyter-config-data" type="application/json">{"allow_hidden_files": false, "appName": "JupyterLab", "appNamespace": "lab", "appSettingsDir": "/Users/lidiamarchese/venv/share/jupyter/lab/settings", "appUrl": "/lab", "appVersion": "4.5.7", "baseUrl": "/", "buildAvailable": true, "buildCheck": true, "cacheFiles": false, "copyAbsolutePath": false, "delete_to_trash": true, "devMode": false, "disabledExtensions": [], "exposeAppInBrowser": false, "extensionManager": {"can_install": true, "install_path": "/Users/lidiamarchese/venv", "name": "PyPI"}, "extraLabextensionsPath": [], "federated_extensions": [{"entrypoints": null, "extension": "./extension", "load": "static/remoteEntry.5cbb9d2323598fbda535.js", "name": "jupyterlab_pygments", "style": "./style"}, {"entrypoints": null, "extension": "./extension", "load": "static/remoteEntry.c632334bd55eee9396d9.js", "name": "@jupyter-notebook/lab-extension", "style": "./style"}, {"entrypoints": null, "extension": "./extension", "load": "static/remoteEntry.9077b3d2deaffb329dfc.js", "name": "@jupyter-widgets/jupyterlab-manager"}], "fullAppUrl": "/lab", "fullLabextensionsUrl": "/lab/extensions", "fullLicensesUrl": "/lab/api/licenses", "fullListingsUrl": "/lab/api/listings", "fullMathjaxUrl": "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js", "fullSettingsUrl": "/lab/api/settings", "fullStaticUrl": "/static/lab", "fullThemesUrl": "/lab/api/themes", "fullTranslationsApiUrl": "/lab/api/translations", "fullTreeUrl": "/lab/tree", "fullWorkspacesApiUrl": "/lab/api/workspaces", "ignorePlugins": [], "labextensionsPath": ["/Users/lidiamarchese/venv/share/jupyter/labextensions", "/Users/lidiamarchese/Library/Jupyter/labextensions", "/usr/local/share/jupyter/labextensions", "/usr/share/jupyter/labextensions"], "labextensionsUrl": "/lab/extensions", "licensesUrl": "/lab/api/licenses", "listingsUrl": "/lab/api/listings", "mathjaxConfig": "TeX-AMS_HTML-full,Safe", "mode": "multiple-document", "nbclassic_enabled": false, "news": {"disabled": false}, "notebookStartsKernel": true, "notebookVersion": "[2, 18, 2]", "preferredPath": "/", "quitButton": true, "rootUri": "file:///Users/lidiamarchese/venv", "schemasDir": "/Users/lidiamarchese/venv/share/jupyter/lab/schemas", "serverRoot": "~/venv", "settingsUrl": "/lab/api/settings", "staticDir": "/Users/lidiamarchese/venv/share/jupyter/lab/static", "store_id": 2, "templatesDir": "/Users/lidiamarchese/venv/share/jupyter/lab/static", "terminalsAvailable": true, "themesDir": "/Users/lidiamarchese/venv/share/jupyter/lab/themes", "themesUrl": "/lab/api/themes", "token": "4213fbde49879524f5c9de87586853a5a95670cbc5cdb44a", "translationsApiUrl": "/lab/api/translations", "treePath": "", "treeUrl": "/lab/tree", "untracked_message_types": ["comm_info_request", "comm_info_reply", "kernel_info_request", "kernel_info_reply", "shutdown_request", "shutdown_reply", "interrupt_request", "interrupt_reply", "debug_request", "debug_reply", "stream", "display_data", "update_display_data", "execute_input", "execute_result", "error", "status", "clear_output", "debug_event", "input_request", "input_reply"], "userSettingsDir": "/Users/lidiamarchese/.jupyter/lab/user-settings", "virtualDocumentsUri": "file:///Users/lidiamarchese/venv/.virtual_documents", "workspace": "default", "workspacesApiUrl": "/lab/api/workspaces", "workspacesDir": "/Users/lidiamarchese/.jupyter/lab/workspaces", "wsUrl": ""}</script><link rel="icon" type="image/x-icon" href="/static/favicons/favicon.ico" class="idle favicon"><link rel="" type="image/x-icon" href="/static/favicons/favicon-busy-1.ico" class="busy favicon"> <script defer="defer" src="/static/lab/main.30eed593f68996dd7fc7.js?v=30eed593f68996dd7fc7"></script></head><body class="jp-ThemedContainer"><script>/* Remove token from URL. */
  (function () {
    var location = window.location;
    var search = location.search;

    // If there is no query string, bail.
    if (search.length <= 1) {
      return;
    }

    // Rebuild the query string without the `token`.
    var query = '?' + search.slice(1).split('&')
      .filter(function (param) { return param.split('=')[0] !== 'token'; })
      .join('&');

    // Rebuild the URL with the new query string.
    var url = location.origin + location.pathname +
      (query !== '?' ? query : '') + location.hash;

    if (url === location.href) {
      return;
    }

    window.history.replaceState({ }, '', url);
  })();</script></body></html>