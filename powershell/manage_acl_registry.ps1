# Script PowerShell
# Author: mohamedkdidi@gmail.com
# Add & Remove ACL from Windows Registry Key via Powershell.

function AddPermission($key, $user) {
    
    $acl = Get-Acl $key

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


    # create the RegistryAccessRule object using all of the objects collected
    $rule         = New-Object System.Security.AccessControl.RegistryAccessRule($idRef, $regRights, $inhFlags, $prFlags, $acType)


    # Add the RegistryAccessRule created in the previous section to the current ACL using the AddAccessRule()
    $acl.SetAccessRule($rule)

    # Commit the new ACL
    $acl | Set-Acl -Path $key

    Write-Host "`n registry access rule has been applied `n " -ForegroundColor Green

    (Get-Acl $key).Access

}

function DeletePermission($key, $user, $domane) {

    $acl = Get-Acl $key
    Write-Output $acl.access

    $rules = $acl.access | Where-Object { 
        $_.IdentityReference -like "$domane\$user"
    }

    ForEach($rule in $rules) {
        $acl.RemoveAccessRule($rule) | Out-Null
        Write-Host "`n rule deleted `n" -ForegroundColor Red 
    }

    Set-ACL -Path $key -AclObject $acl
}


$security_key = "HKLM:\SYSTEM\CurrentControlSet\Services\EventLog\Security"
$user         = $args[0]
$domaine      = $domaine[1]

DeletePermission $security_key $user $domaine
AddPermission $security_key $user