
/** @odoo-module **/

import { UserMenu } from "@web/webclient/user_menu/user_menu";
import { patch } from "@web/core/utils/patch";
import { registry } from "@web/core/registry";



const userMenuRegistry = registry.category("user_menuitems");

// Save the original setup method
const originalSetup = UserMenu.prototype.setup;

patch(UserMenu.prototype, {
    setup() {
        // Call the original setup method
        if (originalSetup) {
            originalSetup.call(this, ...arguments);
        }

        // Removing items from the user menu
        userMenuRegistry.remove("documentation");
        userMenuRegistry.remove("support");
        userMenuRegistry.remove("odoo_account");
        userMenuRegistry.remove("shortcuts");
    },
});


