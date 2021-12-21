# Morpheus Roles as Code

## Variables

`morpheus_url` - Morpheus URL eg. `https://morpheus.example.com`

`morpheus_token` - Morpheus Access Token

`user_roles` - User roles list of dicts

## Workflow

This role checks for the existence of a Morpheus user role, and selects that ID if it exists.  It will create the role if not.  The initial role is created with no permissions, meaning all permissions are `none`.  This means you only have to specify permission bits that you want to grant.

## Example user_roles

The following will create a role with read-only permissions to Morpheus groups and clouds. 

```
user_roles:
    - name: "TestRole1"
      description: "This is a test role for Morpheus"
      role_type: user
      multitenant: "true"
      multitenant_locked: "true"
      role_feature_permissions:
        - code: admin-zones
          access: read
        - code: admin-groups
          access: read
```

## Considerations

This role will re-apply all permissions defined for each role, but if the permission bit is missing, it will not reset to `none`

## Tips to extract roles from Morpheus

Using the Morpheus CLI, it's easy to export the roles in a format that this role is expecting.

Do the following:
```
# Get the id number of the role you want to export
morpheus roles list
# Get role details of description, role type, and multitenant options
morpheus roles get <id>
# Finally format the permission output while filtering out disabled permissions
export ROLEID=<id> && \ 
echo "      role_feature_permissions:" && \ 
morpheus roles list-permissions $ROLEID --csv| gawk -F, '{if ($4 != "none" && $4 != "access") print "        - code: "$2"\n          access: \""$4"\""}'
