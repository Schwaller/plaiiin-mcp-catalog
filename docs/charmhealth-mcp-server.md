An MCP server for CharmHealth EHR that allows LLMs and MCP clients to interact with patient records, encounters, and practice information.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/charmhealth-mcp-server](https://hub.docker.com/repository/docker/mcp/charmhealth-mcp-server)
**Author**|[CharmHealth](https://github.com/CharmHealth)
**Repository**|https://github.com/CharmHealth/charm-mcp-server

## Available Tools (17)
Tools provided by this Server|Short Description
-|-
`findPatients`|Find patients.|
`getPracticeInfo`|Get practice information.|
`manageAppointments`|Manage appointments.|
`manageEncounter`|Manage encounters.|
`manageFax`|Send faxes and check fax delivery status.|
`manageMessages`|Manage patient and provider messaging across SMS, WhatsApp, and secure messaging channels.|
`managePatient`|Manage patients.|
`managePatientAllergies`|Manage patient allergies.|
`managePatientDiagnoses`|Manage patient diagnoses.|
`managePatientDrugs`|Manage patient drugs and supplements.|
`managePatientFiles`|Manage patient files and documents.|
`managePatientLabs`|Manage patient laboratory results.|
`managePatientNotes`|Manage patient notes.|
`managePatientRecalls`|Manage patient recalls.|
`managePatientVitals`|Manage patient vitals and vital signs.|
`manageTasks`|Manage CharmHealth tasks.|
`reviewPatientHistory`|Review patient history.|

---
## Tools Details

#### Tool: **`findPatients`**
Find patients.

<usecase>
Find patients quickly using natural search terms or specific criteria. Handles everything from 
"find John Smith" to complex searches like "elderly diabetes patients in California". 
Essential first step for any patient-related task.
</usecase>

<instructions>
Quick searches: Use search_type="name" with query="John Smith" for basic name searches
Phone lookups: Use search_type="phone" with query="555-1234" (handles any format)
Medical record: Use search_type="record_id" with query="MR123456"

Complex searches: Use search_type="advanced" with multiple criteria:
- Age ranges: age_min=65, age_max=80 for elderly patients
- Location: state="CA", city="Los Angeles" for geographic filtering  
- Medical: blood_group="O+", language="Spanish" for clinical needs

Always returns patient_id needed for other tools. Start here before any patient operations.

When required parameters are missing, ask the user to provide the specific values rather than proceeding with defaults or auto-generated values.
</instructions>
Parameters|Type|Description
-|-|-
`age_max`|`string` *optional*|
`age_min`|`string` *optional*|
`blood_group`|`string` *optional*|
`category_id`|`string` *optional*|
`city`|`string` *optional*|
`country`|`string` *optional*|
`created_after`|`string` *optional*|
`created_before`|`string` *optional*|
`facility_id`|`string` *optional*|
`gender`|`string` *optional*|
`has_phr_account`|`string` *optional*|
`language`|`string` *optional*|
`limit`|`string` *optional*|
`marital_status`|`string` *optional*|
`modified_after`|`string` *optional*|
`modified_before`|`string` *optional*|
`page`|`string` *optional*|
`postal_code`|`string` *optional*|
`query`|`string` *optional*|
`search_type`|`string` *optional*|
`sort_by`|`string` *optional*|
`sort_order`|`string` *optional*|
`state`|`string` *optional*|
`status`|`string` *optional*|

---
#### Tool: **`getPracticeInfo`**
Get practice information.

<usecase>
Get essential practice information needed for other operations - available facilities,
providers, vital signs templates, etc. Use this to understand practice setup and get IDs for other tools.
</usecase>

<instructions>
- "facilities": List all practice locations with IDs needed for scheduling
- "providers": List all providers with IDs needed for appointments and encounters
- "vitals": Available vital sign templates for documentation
- "overview": Summary of practice setup with key counts and recent activity
- "templates": List all available SOAP templates (id, name, type) for the practice
- "template_details": Full template schema (widgets + entries) for given template_ids (comma-separated)

When required parameters are missing, ask the user to provide the specific values rather than proceeding with defaults or auto-generated values.
</instructions>
Parameters|Type|Description
-|-|-
`info_type`|`string` *optional*|
`template_ids`|`string` *optional*|

---
#### Tool: **`manageAppointments`**
Manage appointments.

<usecase>
Complete appointment lifecycle management - schedule new appointments, reschedule existing ones,
cancel appointments, and list appointments with flexible filtering. Handles the full appointment workflow.
</usecase>

<instructions>
Actions:
- "schedule": Create new appointment (requires patient_id, provider_id, facility_id, appointment_date, appointment_time). Check the provider's availability with manageAppointments(action='list') and provider_id, and across all facilities for the provider before suggesting a time.
- "reschedule": Change existing appointment time (requires appointment_id + new scheduling details)
- "cancel": Cancel appointment (requires appointment_id + cancel_reason)
- "list": Show appointments with filtering (requires start_date, end_date_range, facility_ids; optionally filter by status/provider/mode)

Time format: Use 12-hour format like "09:30 AM" or "02:15 PM"
For recurring: Set repetition to "Weekly" or "Daily" and provide frequency + end_date
For double booking: Use provider_double_booking="allow" or resource_double_booking="allow" to override checks
For cancellation: Use delete_type "Current" for single appointment or "Entire" for recurring series

List filters (applied after fetching all appointments in the date range):
- status_filter: e.g., status_filter="Confirmed"
- provider_filter: provider_id or provider_name substring (e.g., provider_filter="12345" or provider_filter="Smith")
- mode_filter: e.g., mode_filter="Video Consult"
- limit: e.g., limit=25

When required parameters are missing, ask the user to provide the specific values rather than proceeding with defaults or auto-generated values.
</instructions>
Parameters|Type|Description
-|-|-
`action`|`string`|
`appointment_date`|`string` *optional*|
`appointment_id`|`string` *optional*|
`appointment_time`|`string` *optional*|
`cancel_reason`|`string` *optional*|
`consent_forms`|`string` *optional*|
`delete_type`|`string` *optional*|
`duration_minutes`|`string` *optional*|
`end_date`|`string` *optional*|
`end_date_range`|`string` *optional*|
`facility_id`|`string` *optional*|
`facility_ids`|`string` *optional*|
`frequency`|`string` *optional*|
`limit`|`string` *optional*|
`member_ids`|`string` *optional*|
`message_to_patient`|`string` *optional*|
`mode`|`string` *optional*|
`mode_filter`|`string` *optional*|
`patient_id`|`string` *optional*|
`provider_double_booking`|`string` *optional*|
`provider_filter`|`string` *optional*|
`provider_id`|`string` *optional*|
`questionnaire`|`string` *optional*|
`reason`|`string` *optional*|
`receipt_id`|`string` *optional*|
`repetition`|`string` *optional*|
`resource_double_booking`|`string` *optional*|
`resource_id`|`string` *optional*|
`start_date`|`string` *optional*|
`status`|`string` *optional*|
`status_filter`|`string` *optional*|
`status_ids`|`string` *optional*|
`visit_type_id`|`string` *optional*|
`weekly_days`|`string` *optional*|

---
#### Tool: **`manageEncounter`**
Manage encounters.

<usecase>
Complete encounter workflow - create, review, and sign encounters with comprehensive clinical documentation.
Essential for clinical workflow from initial documentation through final signature.
</usecase>

<instructions>
Actions:
- "list": List encounters for a patient (requires patient_id; optionally filter by filter_by, start_date, end_date, per_page, page)
- "create": Create new encounter and document clinical findings (default)
- "review": Display complete encounter details for review before signing
- "sign": Electronically sign encounter after review and confirmation
- "unlock": Unlock a previously signed encounter to allow modifications

For creating encounters (two paths):
- From appointment: patient_id + appointment_id (provider/facility/date come from the appointment)
- From scratch: patient_id + provider_id + facility_id + encounter_date
- Optional: visit_type_id, encounter_mode, chief_complaint

For reviewing encounters:
- Requires: patient_id, encounter_id
- Shows comprehensive encounter details including vitals, diagnoses, medications, notes

For signing encounters:
- Requires: patient_id, encounter_id  
- Only use after reviewing and confirming all information is accurate

For unlocking encounters:
- Requires: patient_id, encounter_id, reason
- Used to unlock signed encounters when modifications are needed
- Must provide a valid reason for unlocking the encounter

For updating encounters with template data:
- action="update" with chief_complaint always saved as narrative fallback
- template_ids: comma-separated IDs of templates to attach to the encounter
- entries: JSON array string of populated template entries, e.g. '[{"entry_id":"123","answer":"text"}]'
- Templates are attached first, then entries + chief_complaints saved together
- entry_id values must come from getPracticeInfo(info_type='template_details') — hallucinated IDs are dropped client-side

Recommended workflow:
1. Create encounter: manageEncounter(patient_id, appointment_id, action="create") — or without appointment: manageEncounter(patient_id, provider_id, facility_id, encounter_date, action="create")
2. Add clinical data using managePatientVitals(), managePatientDrugs(), managePatientDiagnoses()
3. Review before signing: manageEncounter(patient_id, encounter_id, action="review")
4. Sign to finalize: manageEncounter(patient_id, encounter_id, action="sign")
5. If modifications needed: manageEncounter(patient_id, encounter_id, reason="reason for changes", action="unlock")

When required parameters are missing, ask the user to provide the specific values rather than proceeding with defaults or auto-generated values.
</instructions>
Parameters|Type|Description
-|-|-
`patient_id`|`string`|
`action`|`string` *optional*|
`appointment_id`|`string` *optional*|
`chief_complaint`|`string` *optional*|
`encounter_date`|`string` *optional*|
`encounter_id`|`string` *optional*|
`encounter_mode`|`string` *optional*|
`end_date`|`string` *optional*|
`entries`|`string` *optional*|
`facility_id`|`string` *optional*|
`filter_by`|`string` *optional*|
`page`|`string` *optional*|
`per_page`|`string` *optional*|
`provider_id`|`string` *optional*|
`reason`|`string` *optional*|
`start_date`|`string` *optional*|
`template_ids`|`string` *optional*|
`visit_type_id`|`string` *optional*|

---
#### Tool: **`manageFax`**
Send faxes and check fax delivery status.

<usecase>
Fax clinical documents (referrals, records, prior auth forms) to providers,
facilities, pharmacies, and insurance companies. Check delivery status of sent faxes.
</usecase>

<instructions>
Actions:
- "send": Fax a document (requires recipient_fax_number, recipient_name, document_content_base64).
  document_content_base64 must be a base64-encoded PDF.
  Optionally include subject, remarks, and reference for the cover page.
  facility_id determines which facility's fax credentials and return number are used.

- "status": Check fax delivery status (requires fax_id).
  Status values: QUEUED, SENT, FAILED, YET_TO_SEND.

Common fax use cases:
- Referral letters to specialists
- Medical records requests
- Prior authorization forms to insurance
- Prescription orders to pharmacies without e-prescribe
</instructions>
Parameters|Type|Description
-|-|-
`action`|`string`|
`document_content_base64`|`string` *optional*|
`facility_id`|`string` *optional*|
`fax_id`|`string` *optional*|
`recipient_fax_number`|`string` *optional*|
`recipient_name`|`string` *optional*|
`reference`|`string` *optional*|
`remarks`|`string` *optional*|
`subject`|`string` *optional*|

---
#### Tool: **`manageMessages`**
Manage patient and provider messaging across SMS, WhatsApp, and secure messaging channels.

<usecase>
Send messages to patients, read inbox messages, and retrieve conversation threads.
Supports SMS (Twilio/Telnyx), WhatsApp Business, and secure portal messaging.
Use this for patient communication, follow-ups, appointment confirmations, and
responding to patient inquiries.
</usecase>

<instructions>
Actions:
- "send": Send a message to a patient (requires patient_id, content, and facility_id).
  Channel options:
    - "sms": Send via text message (patient must have TEXT_NOTIFY_ENABLED)
    - "whatsapp": Send via WhatsApp (patient must be opted in)
    - "secure": Send via secure portal message (requires subject)
    - "auto": Automatically select best available channel (default)
  facility_id is required for all channels. Use getPracticeInfo() to look up facility IDs.
  For WhatsApp templates, provide template_name and placeholder values.
  For secure messages to providers, use recipient_member_ids.

- "list": Show recent secure portal messages from inbox.
  Filter by section: "FROM_PATIENTS" (inbox) or "TO_PATIENTS" (sent).
  Use facility_id to filter by facility.
  Note: SMS and WhatsApp conversations are not available via list — use action='get_thread'
  with a patient_id to retrieve those.

- "get_thread": Get full conversation history with a specific patient (requires patient_id).
  Filter by thread_channel to see only SMS, WhatsApp, secure, or all channels.

Before sending clinical content, confirm with the provider. Routine messages
(appointment reminders, general notifications) can be sent directly.
</instructions>
Parameters|Type|Description
-|-|-
`action`|`string`|
`channel`|`string` *optional*|
`content`|`string` *optional*|
`facility_id`|`string` *optional*|
`message_type`|`string` *optional*|
`page`|`string` *optional*|
`page_size`|`string` *optional*|
`patient_id`|`string` *optional*|
`recipient_member_ids`|`string` *optional*|
`section`|`string` *optional*|
`subject`|`string` *optional*|
`template_body_placeholders`|`string` *optional*|
`template_header_placeholders`|`string` *optional*|
`template_name`|`string` *optional*|
`thread_channel`|`string` *optional*|

---
#### Tool: **`managePatient`**
Manage patients.

<usecase>
Complete patient management with comprehensive demographic, social, and administrative data.
Handles patient creation, updates, status changes, and complex relationships. Supports all 
CharmHealth patient data fields for complete EHR functionality.
</usecase>

<instructions>
Actions:
- "create": Add new patient (requires first_name, last_name, gender, date_of_birth OR age, facility_ids)
- "update": Modify existing patient (requires patient_id + fields to change).
- "activate": Reactivate deactivated patient (requires patient_id only)
- "deactivate": Deactivate patient (requires patient_id only)

Update Modes:
- update_specific_details=True: Only updates the fields you provide, preserves all other existing data (RECOMMENDED, Default)
- update_specific_details=False: Complete record update - must provide all fields or existing data will be lost

Demographics: Supports comprehensive patient information including social history, family data
Addresses: If any address field provided, country is required (defaults to US)
Facilities: Pass as list of facility IDs like "facility_123,facility_456".
Categories: Pass as list like [{"category_id": "category_123"}]

Complex Relationships:
- caregivers: [{"first_name": str, "last_name": str, "relationship": str, "contact": {...}, "address": {...}}]
- guarantor: [{"first_name": str, "last_name": str, "relationship": str, "contact": {...}, "address": {...}}]
- id_qualifiers: [{"id_qualifier": 1-8 or 99, "id_of_patient": "ID_value"}]

When required parameters are missing, ask the user to provide the specific values rather than proceeding with defaults or auto-generated values.
</instructions>
Parameters|Type|Description
-|-|-
`action`|`string`|
`address_line1`|`string` *optional*|
`address_line2`|`string` *optional*|
`age`|`string` *optional*|
`area`|`string` *optional*|
`birth_order`|`string` *optional*|
`blood_group`|`string` *optional*|
`caregivers`|`string` *optional*|
`categories`|`string` *optional*|Categories: Pass as list like [{"category_id": "category_123"}]
`cause_of_death`|`string` *optional*|
`city`|`string` *optional*|
`country`|`string` *optional*|
`county_code`|`string` *optional*|
`custom_field_1`|`string` *optional*|
`custom_field_2`|`string` *optional*|
`custom_field_3`|`string` *optional*|
`custom_field_4`|`string` *optional*|
`custom_field_5`|`string` *optional*|
`date_of_birth`|`string` *optional*|
`deceased`|`string` *optional*|
`district`|`string` *optional*|
`dod`|`string` *optional*|
`duplicate_check`|`string` *optional*|
`email`|`string` *optional*|
`email_notification`|`string` *optional*|
`emergency_contact_name`|`string` *optional*|
`emergency_contact_phone`|`string` *optional*|
`emergency_extn`|`string` *optional*|
`employment_status`|`string` *optional*|
`ethnicity`|`string` *optional*|
`facility_ids`|`string` *optional*|
`first_name`|`string` *optional*|
`gender`|`string` *optional*|
`gender_identity`|`string` *optional*|
`guarantor`|`string` *optional*|
`home_phone`|`string` *optional*|
`id_qualifiers`|`string` *optional*|
`introduction`|`string` *optional*|
`is_multiple_birth`|`string` *optional*|
`language`|`string` *optional*|
`last_name`|`string` *optional*|
`linked_patient_id`|`string` *optional*|
`maiden_name`|`string` *optional*|
`marital_status`|`string` *optional*|
`middle_name`|`string` *optional*|
`mother_first_name`|`string` *optional*|
`mother_last_name`|`string` *optional*|
`nick_name`|`string` *optional*|
`patient_id`|`string` *optional*|
`payment_end_date`|`string` *optional*|
`payment_source`|`string` *optional*|
`payment_start_date`|`string` *optional*|
`phone`|`string` *optional*|
`post_box`|`string` *optional*|
`preferred_communication`|`string` *optional*|
`primary_phone`|`string` *optional*|
`race`|`string` *optional*|
`record_id`|`string` *optional*|
`rep_first_name`|`string` *optional*|
`rep_last_name`|`string` *optional*|
`send_phr_invite`|`string` *optional*|
`sexual_orientation`|`string` *optional*|
`smoking_status`|`string` *optional*|
`source_name`|`string` *optional*|
`source_value`|`string` *optional*|
`state`|`string` *optional*|
`suffix`|`string` *optional*|
`text_notification`|`string` *optional*|
`update_specific_details`|`string` *optional*|
`voice_notification`|`string` *optional*|
`work_phone`|`string` *optional*|
`work_phone_extn`|`string` *optional*|
`zip_code`|`string` *optional*|

---
#### Tool: **`managePatientAllergies`**
Manage patient allergies.

<usecase>
Critical allergy management with safety alerts - document patient allergies, update allergy information,
and maintain allergy safety checks. Essential for safe prescribing and clinical decision-making.
</usecase>

<instructions>
Actions:
- "add": Document new allergy (requires allergen, allergy_type, severity, reactions, allergy_date)
- "list": Show all patient allergies (optionally filter by severity/type)
- "update": Modify existing allergy (requires record_id, allergen, allergy_type, severity, allergy_status — use action='list' first to get current values, then pass all required fields with your changes)
- "delete": Remove allergy record (requires record_id)

Safety critical: Always check allergies before prescribing medications.
Common allergens: "Penicillin", "Latex", "Shellfish", "Nuts", "Contrast dye"
Severity levels: "Mild", "Moderate", "Severe"
Allergy types: "Medication", "Drug Substance", "Environmental", "Food", "Plant", "Animal", "Latex"
Status values: "Active", "Inactive"

List filters:
- severity_filter: e.g., severity_filter="Severe"
- type_filter: e.g., type_filter="Drug"
- limit: e.g., limit=50

When required parameters are missing, ask the user to provide the specific values rather than proceeding with defaults or auto-generated values.
</instructions>
Parameters|Type|Description
-|-|-
`action`|`string`|
`patient_id`|`string`|
`allergen`|`string` *optional*|
`allergy_date`|`string` *optional*|
`allergy_status`|`string` *optional*|
`allergy_type`|`string` *optional*|
`comments`|`string` *optional*|
`limit`|`string` *optional*|
`reactions`|`string` *optional*|
`record_id`|`string` *optional*|
`severity`|`string` *optional*|
`severity_filter`|`string` *optional*|
`type_filter`|`string` *optional*|

---
#### Tool: **`managePatientDiagnoses`**
Manage patient diagnoses.

<usecase>
Complete diagnosis management for patient problem lists - add new diagnoses, update existing conditions,
and maintain accurate medical problem lists. Essential for clinical reasoning and care planning.
</usecase>

<instructions>
Actions:
- "add": Add new diagnosis (requires diagnosis_name, diagnosis_code, code_type)
- "list": Show all patient diagnoses (optionally filter by status, code type, and/or date range)
- "update": Modify existing diagnosis (requires record_id + fields to change)
- "delete": Remove diagnosis (requires record_id). Ask the user if they are sure they want to delete the diagnosis before proceeding.

Code types: "ICD10", "SNOMED"
Status options: "Active", "Inactive", "Resolved"
List filters:
- status_filter: filter by diagnosis_status (e.g., status_filter="Active")
- code_type_filter: filter by code_type (e.g., code_type_filter="ICD10")
- from_date / to_date: best-effort date filtering (e.g., from_date="2025-01-01", to_date="2025-12-31")
- limit: e.g., limit=25
Use encounter_id to link diagnosis to specific visit for billing and documentation

When required parameters are missing, ask the user to provide the specific values rather than proceeding with defaults or auto-generated values.
</instructions>
Parameters|Type|Description
-|-|-
`action`|`string`|
`patient_id`|`string`|
`code_type`|`string` *optional*|
`code_type_filter`|`string` *optional*|
`comments`|`string` *optional*|
`diagnosis_code`|`string` *optional*|
`diagnosis_name`|`string` *optional*|
`diagnosis_order`|`string` *optional*|
`diagnosis_status`|`string` *optional*|
`encounter_id`|`string` *optional*|
`from_date`|`string` *optional*|
`limit`|`string` *optional*|
`record_id`|`string` *optional*|
`status_filter`|`string` *optional*|
`to_date`|`string` *optional*|

---
#### Tool: **`managePatientDrugs`**
Manage patient drugs and supplements.

<usecase>
Unified drug management for medications, supplements, and vitamins - prescribe medications, 
document supplements, manage drug interactions. Includes automatic allergy checking and 
comprehensive drug safety workflow for optimal patient care.
</usecase>

<instructions>
Actions:
- "add": Prescribe new drug (requires drug_name, directions for medications; drug_name, dosage for supplements)
- "update": Modify existing prescription (requires record_id + fields to change). IMPORTANT: drug name and strength CANNOT be changed via update — use discontinue + add instead. Updatable fields: directions, dispense, refills, status.
- "discontinue": Stop drug (requires record_id)
- "list": Show all patient drugs by type (filter by substance_type, optionally filter by status)

Substance Types:
- "medication": Prescription drugs (requires directions, refills)
- "supplement": OTC supplements/vitamins (requires dosage as integer)
- "vitamin": Specific vitamins (requires dosage as integer)

Safety: Automatically checks allergies before prescribing unless check_allergies=False
List filters:
- status_filter: e.g., status_filter="active"
- limit: e.g., limit=25
For medications: Use clear directions like "Take 1 tablet by mouth twice daily with food"
For supplements: Provide dosage as integer (e.g., 5) and use strength for units (e.g., "500mg")

When required parameters are missing, ask the user to provide the specific values rather than proceeding with defaults or auto-generated values.
</instructions>
Parameters|Type|Description
-|-|-
`action`|`string`|
`patient_id`|`string`|
`check_allergies`|`string` *optional*|
`comments`|`string` *optional*|
`directions`|`string` *optional*|
`dosage`|`string` *optional*|
`dosage_unit`|`string` *optional*|
`dose_form`|`string` *optional*|
`drug_name`|`string` *optional*|
`encounter_id`|`string` *optional*|
`end_date`|`st

[...]
