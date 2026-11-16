# Report comments
Revision 3. Product behavior approved; technical planning and saving planning documents authorized. Implementation and deployment are not authorized.
Project readers can create and read comments on reports. Readers outside the project cannot read or add comments. Keep this internal unless doing so costs substantially more. No editing or deletion UI in this increment.
Engineering chooses what happens when reports are deleted or renamed. Retaining rows was suggested only to avoid cleanup; restoration is not required.
Technical proposal: use the existing API storage connection. This is not an owner commitment; verify architecture before adopting it.
Acceptance: an authorized reader creates a comment and reads it back; an unauthorized reader cannot create or retrieve it. No specific save acknowledgement timing has been agreed.
