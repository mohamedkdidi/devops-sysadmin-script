# Script PowerShell
# Author: mohamedkdidi@gmail.com
# Giving service account or application access to EventLog Windows.

$eventLog_key = "HKLM:\SYSTEM\CurrentControlSet\Services\EventLog"
$security_key = "HKLM:\SYSTEM\CurrentControlSet\Services\EventLog\Security"
$user         = "your service account name"

$acl_eventLog = Get-Acl $eventLog_key
$acl_security = Get-Acl $security_key

# Create the identity
$idRef        = [System.Security.Principal.NTAccount]($user)

# Create a System.Security.AccessControl.RegistryRights object using the appropriate rights 
$regRights    = [System.Security.AccessControl.RegistryRights]::FullControl

# InheritanceFlags Enum (ContainerInherit | None | ObjectInherit)
# https://docs.microsoft.com/en-us/dotnet/api/system.security.accesscontrol.inheritanceflags?view=netframework-4.8
$inhFlags     = [System.Security.AccessControl.InheritanceFlags]::ContainerInherit 

$prFlags      = [System.Security.AccessControl.PropagationFlags]::None 

# AccessControlType Enum (Allow | Deny)
# https://docs.microsoft.com/en-us/dotnet/api/system.security.accesscontrol.accesscontroltype?view=netframework-4.8
$acType       = [System.Security.AccessControl.AccessControlType]::Allow 


# Create the RegistryAccessRule object using all of the objects collected
$rule         = New-Object System.Security.AccessControl.RegistryAccessRule($idRef, $regRights, $inhFlags, $prFlags, $acType)


# Add the RegistryAccessRule created in the previous section to the current ACL using the AddAccessRule()
$acl_eventLog.AddAccessRule($rule)

# Commit the new ACL
$acl_eventLog | Set-Acl -Path $eventLog_key


$acl_security.AddAccessRule($rule)

$acl_security | Set-Acl -Path $security_key

Write-Debug "registry access rule has been applied"

# (Get-Acl $eventLog_key).Access

# (Get-Acl $security_key).Access