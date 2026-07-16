Interact with Hostinger services over the Hostinger API.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/api-mcp-server](https://hub.docker.com/repository/docker/mcp/api-mcp-server)
**Author**|[hostinger](https://github.com/hostinger)
**Repository**|https://github.com/hostinger/api-mcp-server

## Available Tools (118)
Tools provided by this Server|Short Description
-|-
`DNS_deleteDNSRecordsV1`|Delete DNS records for the selected domain.|
`DNS_getDNSRecordsV1`|Retrieve DNS zone records for a specific domain.|
`DNS_getDNSSnapshotListV1`|Retrieve DNS snapshots for a domain.|
`DNS_getDNSSnapshotV1`|Retrieve particular DNS snapshot with contents of DNS zone records.|
`DNS_resetDNSRecordsV1`|Reset DNS zone to the default records.|
`DNS_restoreDNSSnapshotV1`|Restore DNS zone to the selected snapshot.|
`DNS_updateDNSRecordsV1`|Update DNS records for the selected domain.|
`DNS_validateDNSRecordsV1`|Validate DNS records prior to update for the selected domain.|
`VPS_activateFirewallV1`|Activate a firewall for a specified virtual machine.|
`VPS_attachPublicKeyV1`|Attach existing public keys from your account to a specified virtual machine.|
`VPS_createFirewallRuleV1`|Create new firewall rule for a specified firewall.|
`VPS_createNewFirewallV1`|Create a new firewall.|
`VPS_createNewProjectV1`|Deploy new project from docker-compose.yaml contents or download contents from URL.|
`VPS_createPTRRecordV1`|Create or update a PTR (Pointer) record for a specified virtual machine.|
`VPS_createPostInstallScriptV1`|Add a new post-install script to your account, which can then be used after virtual machine installation.|
`VPS_createPublicKeyV1`|Add a new public key to your account.|
`VPS_createSnapshotV1`|Create a snapshot of a specified virtual machine.|
`VPS_deactivateFirewallV1`|Deactivate a firewall for a specified virtual machine.|
`VPS_deleteFirewallRuleV1`|Delete a specific firewall rule from a specified firewall.|
`VPS_deleteFirewallV1`|Delete a specified firewall.|
`VPS_deletePTRRecordV1`|Delete a PTR (Pointer) record for a specified virtual machine.|
`VPS_deletePostInstallScriptV1`|Delete a post-install script from your account.|
`VPS_deleteProjectV1`|Completely removes a Docker Compose project from the virtual machine, stopping all containers and cleaning up associated resources including networks, volumes, and images.|
`VPS_deletePublicKeyV1`|Delete a public key from your account.|
`VPS_deleteSnapshotV1`|Delete a snapshot of a specified virtual machine.|
`VPS_getActionDetailsV1`|Retrieve detailed information about a specific action performed on a specified virtual machine.|
`VPS_getActionsV1`|Retrieve actions performed on a specified virtual machine.|
`VPS_getAttachedPublicKeysV1`|Retrieve public keys attached to a specified virtual machine.|
`VPS_getBackupsV1`|Retrieve backups for a specified virtual machine.|
`VPS_getDataCenterListV1`|Retrieve all available data centers.|
`VPS_getFirewallDetailsV1`|Retrieve firewall by its ID and rules associated with it.|
`VPS_getFirewallListV1`|Retrieve all available firewalls.|
`VPS_getMetricsV1`|Retrieve historical metrics for a specified virtual machine.|
`VPS_getPostInstallScriptV1`|Retrieve post-install script by its ID.|
`VPS_getPostInstallScriptsV1`|Retrieve post-install scripts associated with your account.|
`VPS_getProjectContainersV1`|Retrieves a list of all containers belonging to a specific Docker Compose project on the virtual machine.|
`VPS_getProjectContentsV1`|Retrieves the complete project information including the docker-compose.yml file contents, project metadata, and current deployment status.|
`VPS_getProjectListV1`|Retrieves a list of all Docker Compose projects currently deployed on the virtual machine.|
`VPS_getProjectLogsV1`|Retrieves aggregated log entries from all services within a Docker Compose project.|
`VPS_getPublicKeysV1`|Retrieve public keys associated with your account.|
`VPS_getScanMetricsV1`|Retrieve scan metrics for the [Monarx](https://www.monarx.com/) malware scanner installed on a specified virtual machine.|
`VPS_getSnapshotV1`|Retrieve snapshot for a specified virtual machine.|
`VPS_getTemplateDetailsV1`|Retrieve detailed information about a specific OS template for virtual machines.|
`VPS_getTemplatesV1`|Retrieve available OS templates for virtual machines.|
`VPS_getVirtualMachineDetailsV1`|Retrieve detailed information about a specified virtual machine.|
`VPS_getVirtualMachinesV1`|Retrieve all available virtual machines.|
`VPS_installMonarxV1`|Install the Monarx malware scanner on a specified virtual machine.|
`VPS_purchaseNewVirtualMachineV1`|Purchase and setup a new virtual machine.|
`VPS_recreateVirtualMachineV1`|Recreate a virtual machine from scratch.|
`VPS_resetHostnameV1`|Reset hostname and PTR record of a specified virtual machine to default value.|
`VPS_restartProjectV1`|Restarts all services in a Docker Compose project by stopping and starting containers in the correct dependency order.|
`VPS_restartVirtualMachineV1`|Restart a specified virtual machine by fully stopping and starting it.|
`VPS_restoreBackupV1`|Restore a backup for a specified virtual machine.|
`VPS_restoreSnapshotV1`|Restore a specified virtual machine to a previous state using a snapshot.|
`VPS_setHostnameV1`|Set hostname for a specified virtual machine.|
`VPS_setNameserversV1`|Set nameservers for a specified virtual machine.|
`VPS_setPanelPasswordV1`|Set panel password for a specified virtual machine.|
`VPS_setRootPasswordV1`|Set root password for a specified virtual machine.|
`VPS_setupPurchasedVirtualMachineV1`|Setup newly purchased virtual machine with `initial` state.|
`VPS_startProjectV1`|Starts all services in a Docker Compose project that are currently stopped.|
`VPS_startRecoveryModeV1`|Initiate recovery mode for a specified virtual machine.|
`VPS_startVirtualMachineV1`|Start a specified virtual machine.|
`VPS_stopProjectV1`|Stops all running services in a Docker Compose project while preserving container configurations and data volumes.|
`VPS_stopRecoveryModeV1`|Stop recovery mode for a specified virtual machine.|
`VPS_stopVirtualMachineV1`|Stop a specified virtual machine.|
`VPS_syncFirewallV1`|Sync a firewall for a specified virtual machine.|
`VPS_uninstallMonarxV1`|Uninstall the Monarx malware scanner on a specified virtual machine.|
`VPS_updateFirewallRuleV1`|Update a specific firewall rule from a specified firewall.|
`VPS_updatePostInstallScriptV1`|Update a specific post-install script.|
`VPS_updateProjectV1`|Updates a Docker Compose project by pulling the latest image versions and recreating containers with new configurations.|
`billing_deletePaymentMethodV1`|Delete a payment method from your account.|
`billing_disableAutoRenewalV1`|Disable auto-renewal for a subscription.|
`billing_enableAutoRenewalV1`|Enable auto-renewal for a subscription.|
`billing_getCatalogItemListV1`|Retrieve catalog items available for order.|
`billing_getPaymentMethodListV1`|Retrieve available payment methods that can be used for placing new orders.|
`billing_getSubscriptionListV1`|Retrieve a list of all subscriptions associated with your account.|
`billing_setDefaultPaymentMethodV1`|Set the default payment method for your account.|
`domains_checkDomainAvailabilityV1`|Check availability of domain names across multiple TLDs.|
`domains_createDomainForwardingV1`|Create domain forwarding configuration.|
`domains_createWHOISProfileV1`|Create WHOIS contact profile.|
`domains_deleteDomainForwardingV1`|Delete domain forwarding data.|
`domains_deleteWHOISProfileV1`|Delete WHOIS contact profile.|
`domains_disableDomainLockV1`|Disable domain lock for the domain.|
`domains_disablePrivacyProtectionV1`|Disable privacy protection for the domain.|
`domains_enableDomainLockV1`|Enable domain lock for the domain.|
`domains_enablePrivacyProtectionV1`|Enable privacy protection for the domain.|
`domains_getDomainDetailsV1`|Retrieve detailed information for specified domain.|
`domains_getDomainForwardingV1`|Retrieve domain forwarding data.|
`domains_getDomainListV1`|Retrieve all domains associated with your account.|
`domains_getWHOISProfileListV1`|Retrieve WHOIS contact profiles.|
`domains_getWHOISProfileUsageV1`|Retrieve domain list where provided WHOIS contact profile is used.|
`domains_getWHOISProfileV1`|Retrieve a WHOIS contact profile.|
`domains_purchaseNewDomainV1`|Purchase and register a new domain name.|
`domains_updateDomainNameserversV1`|Set nameservers for a specified domain.|
`hosting_createWebsiteV1`|Create a new website for the authenticated client.|
`hosting_deployJsApplication`|Deploy a JavaScript application from an archive file to a hosting server.|
`hosting_deployStaticWebsite`|Deploy a static website from an archive file to a hosting server.|
`hosting_deployWordpressPlugin`|Deploy a WordPress plugin from a directory to a hosting server.|
`hosting_deployWordpressTheme`|Deploy a WordPress theme from a directory to a hosting server.|
`hosting_generateAFreeSubdomainV1`|Generate a unique free subdomain that can be used for hosting services without purchasing custom domains.|
`hosting_importWordpressWebsite`|Import a WordPress website from an archive file to a hosting server.|
`hosting_listAvailableDatacentersV1`|Retrieve a list of datacenters available for setting up hosting plans based on available datacenter capacity and hosting plan of your order.|
`hosting_listJsDeployments`|List javascript application deployments for checking their status.|
`hosting_listOrdersV1`|Retrieve a paginated list of orders accessible to the authenticated client.|
`hosting_listWebsitesV1`|Retrieve a paginated list of websites (main and addon types) accessible to the authenticated client.|
`hosting_showJsDeploymentLogs`|Retrieve logs for a specified JavaScript application deployment for debugging purposes in case of failure.|
`hosting_verifyDomainOwnershipV1`|Verify ownership of a single domain and return the verification status.|
`reach_createANewContactSegmentV1`|Create a new contact segment.|
`reach_createANewContactV1`|Create a new contact in the email marketing system.|
`reach_createNewContactsV1`|Create a new contact in the email marketing system.|
`reach_deleteAContactV1`|Delete a contact with the specified UUID.|
`reach_getSegmentDetailsV1`|Get details of a specific segment.|
`reach_listContactGroupsV1`|Get a list of all contact groups.|
`reach_listContactsV1`|Get a list of contacts, optionally filtered by group and subscription status.|
`reach_listProfilesV1`|This endpoint returns all profiles available to the client, including their basic information.|
`reach_listSegmentContactsV1`|Retrieve contacts associated with a specific segment.|
`reach_listSegmentsV1`|Get a list of all contact segments.|
`v2_getDomainVerificationsDIRECT`|Retrieve a list of pending and completed domain verifications.|

---
## Tools Details

#### Tool: **`DNS_deleteDNSRecordsV1`**
Delete DNS records for the selected domain.

To filter which records to delete, add the `name` of the record and `type` to the filter. 
Multiple filters can be provided with single request.

If you have multiple records with the same name and type, and you want to delete only part of them,
refer to the `Update zone records` endpoint.

Use this endpoint to remove specific DNS records from domains.
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name

---
#### Tool: **`DNS_getDNSRecordsV1`**
Retrieve DNS zone records for a specific domain.

Use this endpoint to view current DNS configuration for domain management.
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name

---
#### Tool: **`DNS_getDNSSnapshotListV1`**
Retrieve DNS snapshots for a domain.

Use this endpoint to view available DNS backup points for restoration.
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name

---
#### Tool: **`DNS_getDNSSnapshotV1`**
Retrieve particular DNS snapshot with contents of DNS zone records.

Use this endpoint to view historical DNS configurations for domains.
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name
`snapshotId`|`integer`|Snapshot ID

---
#### Tool: **`DNS_resetDNSRecordsV1`**
Reset DNS zone to the default records.

Use this endpoint to restore domain DNS to original configuration.
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name
`reset_email_records`|`boolean` *optional*|Determines if email records should be reset
`sync`|`boolean` *optional*|Determines if operation should be run synchronously
`whitelisted_record_types`|`array` *optional*|Specifies which record types to not reset

---
#### Tool: **`DNS_restoreDNSSnapshotV1`**
Restore DNS zone to the selected snapshot.

Use this endpoint to revert domain DNS to a previous configuration.
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name
`snapshotId`|`integer`|Snapshot ID

---
#### Tool: **`DNS_updateDNSRecordsV1`**
Update DNS records for the selected domain.

Using `overwrite = true` will replace existing records with the provided ones. 
Otherwise existing records will be updated and new records will be added.

Use this endpoint to modify domain DNS configuration.
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name
`zone`|`array`|zone parameter
`overwrite`|`boolean` *optional*|If `true`, resource records (RRs) matching name and type will be deleted and new RRs will be created,
otherwise resource records' ttl's are updated and new records are appended.
If no matching RRs are found, they are created.

---
#### Tool: **`DNS_validateDNSRecordsV1`**
Validate DNS records prior to update for the selected domain.

If the validation is successful, the response will contain `200 Success` code.
If there is validation error, the response will fail with `422 Validation error` code.

Use this endpoint to verify DNS record validity before applying changes.
Parameters|Type|Description
-|-|-
`domain`|`string`|Domain name
`zone`|`array`|zone parameter
`overwrite`|`boolean` *optional*|If `true`, resource records (RRs) matching name and type will be deleted and new RRs will be created,
otherwise resource records' ttl's are updated and new records are appended.
If no matching RRs are found, they are created.

---
#### Tool: **`VPS_activateFirewallV1`**
Activate a firewall for a specified virtual machine.

Only one firewall can be active for a virtual machine at a time.

Use this endpoint to apply firewall rules to VPS instances.
Parameters|Type|Description
-|-|-
`firewallId`|`integer`|Firewall ID
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_attachPublicKeyV1`**
Attach existing public keys from your account to a specified virtual machine.

Multiple keys can be attached to a single virtual machine.

Use this endpoint to enable SSH key authentication for VPS instances.
Parameters|Type|Description
-|-|-
`ids`|`array`|Public Key IDs to attach
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_createFirewallRuleV1`**
Create new firewall rule for a specified firewall.

By default, the firewall drops all incoming traffic,
which means you must add accept rules for all ports you want to use.

Any virtual machine that has this firewall activated will lose sync with the firewall
and will have to be synced again manually.

Use this endpoint to add new security rules to firewalls.
Parameters|Type|Description
-|-|-
`firewallId`|`integer`|Firewall ID
`port`|`string`|Port or port range, ex: 1024:2048
`protocol`|`string`|protocol parameter
`source`|`string`|source parameter
`source_detail`|`string`|IP range, CIDR, single IP or `any`

---
#### Tool: **`VPS_createNewFirewallV1`**
Create a new firewall.

Use this endpoint to set up new firewall configurations for VPS security.
Parameters|Type|Description
-|-|-
`name`|`string`|name parameter

---
#### Tool: **`VPS_createNewProjectV1`**
Deploy new project from docker-compose.yaml contents or download contents from URL. 

URL can be Github repository url in format https://github.com/[user]/[repo]
and it will be automatically resolved to docker-compose.yaml file in
master branch. Any other URL provided must return docker-compose.yaml
file contents.

If project with the same name already exists, existing project will be replaced.
Parameters|Type|Description
-|-|-
`content`|`string`|URL pointing to docker-compose.yaml file, Github repository or raw YAML content of the compose file
`project_name`|`string`|Docker Compose project name using alphanumeric characters, dashes, and underscores only
`virtualMachineId`|`integer`|Virtual Machine ID
`environment`|`string` *optional*|Project environment variables

---
#### Tool: **`VPS_createPTRRecordV1`**
Create or update a PTR (Pointer) record for a specified virtual machine.

Use this endpoint to configure reverse DNS lookup for VPS IP addresses.
Parameters|Type|Description
-|-|-
`domain`|`string`|Pointer record domain
`ipAddressId`|`integer`|IP Address ID
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_createPostInstallScriptV1`**
Add a new post-install script to your account, which can then be used after virtual machine installation.

The script contents will be saved to the file `/post_install` with executable attribute set
and will be executed once virtual machine is installed.
The output of the script will be redirected to `/post_install.log`. Maximum script size is 48KB.

Use this endpoint to create automation scripts for VPS setup tasks.
Parameters|Type|Description
-|-|-
`content`|`string`|Content of the script
`name`|`string`|Name of the script

---
#### Tool: **`VPS_createPublicKeyV1`**
Add a new public key to your account.

Use this endpoint to register SSH keys for VPS authentication.
Parameters|Type|Description
-|-|-
`key`|`string`|key parameter
`name`|`string`|name parameter

---
#### Tool: **`VPS_createSnapshotV1`**
Create a snapshot of a specified virtual machine.

A snapshot captures the state and data of the virtual machine at a specific point in time, 
allowing users to restore the virtual machine to that state if needed. 
This operation is useful for backup purposes, system recovery, 
and testing changes without affecting the current state of the virtual machine.

**Creating new snapshot will overwrite the existing snapshot!**

Use this endpoint to capture VPS state for backup and recovery purposes.
Parameters|Type|Description
-|-|-
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_deactivateFirewallV1`**
Deactivate a firewall for a specified virtual machine.

Use this endpoint to remove firewall protection from VPS instances.
Parameters|Type|Description
-|-|-
`firewallId`|`integer`|Firewall ID
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_deleteFirewallRuleV1`**
Delete a specific firewall rule from a specified firewall.

Any virtual machine that has this firewall activated will lose sync with the firewall
and will have to be synced again manually.

Use this endpoint to remove specific firewall rules.
Parameters|Type|Description
-|-|-
`firewallId`|`integer`|Firewall ID
`ruleId`|`integer`|Firewall Rule ID

---
#### Tool: **`VPS_deleteFirewallV1`**
Delete a specified firewall.

Any virtual machine that has this firewall activated will automatically have it deactivated.

Use this endpoint to remove unused firewall configurations.
Parameters|Type|Description
-|-|-
`firewallId`|`integer`|Firewall ID

---
#### Tool: **`VPS_deletePTRRecordV1`**
Delete a PTR (Pointer) record for a specified virtual machine.

Once deleted, reverse DNS lookups to the virtual machine's IP address will
no longer return the previously configured hostname.

Use this endpoint to remove reverse DNS configuration from VPS instances.
Parameters|Type|Description
-|-|-
`ipAddressId`|`integer`|IP Address ID
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_deletePostInstallScriptV1`**
Delete a post-install script from your account.

Use this endpoint to remove unused automation scripts.
Parameters|Type|Description
-|-|-
`postInstallScriptId`|`integer`|Post-install script ID

---
#### Tool: **`VPS_deleteProjectV1`**
Completely removes a Docker Compose project from the virtual machine, stopping all containers and cleaning up 
associated resources including networks, volumes, and images. 

This operation is irreversible and will delete all project data. 

Use this when you want to permanently remove a project and free up system resources.
Parameters|Type|Description
-|-|-
`projectName`|`string`|Docker Compose project name using alphanumeric characters, dashes, and underscores only
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_deletePublicKeyV1`**
Delete a public key from your account. 

**Deleting public key from account does not remove it from virtual machine** 

Use this endpoint to remove unused SSH keys from account.
Parameters|Type|Description
-|-|-
`publicKeyId`|`integer`|Public Key ID

---
#### Tool: **`VPS_deleteSnapshotV1`**
Delete a snapshot of a specified virtual machine.

Use this endpoint to remove VPS snapshots.
Parameters|Type|Description
-|-|-
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_getActionDetailsV1`**
Retrieve detailed information about a specific action performed on a specified virtual machine.

Use this endpoint to monitor specific VPS operation status and details.
Parameters|Type|Description
-|-|-
`actionId`|`integer`|Action ID
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_getActionsV1`**
Retrieve actions performed on a specified virtual machine.

Actions are operations or events that have been executed on the virtual
machine, such as starting, stopping, or modifying the machine. This endpoint
allows you to view the history of these actions, providing details about
each action, such as the action name, timestamp, and status.

Use this endpoint to view VPS operation history and troubleshoot issues.
Parameters|Type|Description
-|-|-
`virtualMachineId`|`integer`|Virtual Machine ID
`page`|`integer` *optional*|Page number

---
#### Tool: **`VPS_getAttachedPublicKeysV1`**
Retrieve public keys attached to a specified virtual machine.

Use this endpoint to view SSH keys configured for specific VPS instances.
Parameters|Type|Description
-|-|-
`virtualMachineId`|`integer`|Virtual Machine ID
`page`|`integer` *optional*|Page number

---
#### Tool: **`VPS_getBackupsV1`**
Retrieve backups for a specified virtual machine.

Use this endpoint to view available backup points for VPS data recovery.
Parameters|Type|Description
-|-|-
`virtualMachineId`|`integer`|Virtual Machine ID
`page`|`integer` *optional*|Page number

---
#### Tool: **`VPS_getDataCenterListV1`**
Retrieve all available data centers.

Use this endpoint to view location options before deploying VPS instances.
#### Tool: **`VPS_getFirewallDetailsV1`**
Retrieve firewall by its ID and rules associated with it.

Use this endpoint to view specific firewall configuration and rules.
Parameters|Type|Description
-|-|-
`firewallId`|`integer`|Firewall ID

---
#### Tool: **`VPS_getFirewallListV1`**
Retrieve all available firewalls.

Use this endpoint to view existing firewall configurations.
Parameters|Type|Description
-|-|-
`page`|`integer` *optional*|Page number

---
#### Tool: **`VPS_getMetricsV1`**
Retrieve historical metrics for a specified virtual machine.

It includes the following metrics: 
- CPU usage
- Memory usage
- Disk usage
- Network usage
- Uptime

Use this endpoint to monitor VPS performance and resource utilization over time.
Parameters|Type|Description
-|-|-
`date_from`|`string`|date_from parameter
`date_to`|`string`|date_to parameter
`virtualMachineId`|`integer`|Virtual Machine ID

---
#### Tool: **`VPS_getPostInstallScriptV1`**
Retrieve post-install script by its ID.

Use this endpoint to view specific automation script details.
Parameters|Type|Description
-|-|-
`postInstallScriptId`|`integer`|Post-install script ID

---
#### Tool: **`VPS_getPostInstallScriptsV1`**
Retrieve post-install scripts associated with your account.

Use this endpoint to view available automation scripts for VPS deployment.
Parameters|Type|Description
-|-|-
`page`|`integer` *optional*|Page number

---
#### Tool: **`VPS_getProjectContainersV1`**
Retrieves a list of all containers belonging to a specific Docker

[...]
