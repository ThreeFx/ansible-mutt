## `ansible-mutt`

Vars prefix: `mail_`

Ansible role to configure E-Mail accounts using `mutt` as client and `offlineimap`
for syncing. Tested on Debian 9 (Stretch), support for other releases or OSes
not guaranteed.

Put your mail passwords in `{{ mail_secrets_dir }}/{{ account_name }}` for each
account to finalize the configuration. This can for example be located on an
encfs for extra security. This step (obviously) has to be completed manually.
