{
    "name": "Accounting Foreign Exchange",
    "version": "1.0",
    "category": "Accounting",
    "summary": "Foreign Exchange in Accounting Transactions",
    "sequence": 1,
    "depends": ["account", "base"],
    "data": [
        "security/ir.model.access.csv",
        "views/actions.xml",
        "views/menus.xml",
        "views/foreign_exchange_rate_views.xml",
    ],
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}
