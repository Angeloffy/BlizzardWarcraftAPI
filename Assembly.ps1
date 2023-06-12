$path = Get-Location
$pathVenv = $path.tostring() + "\venv"
$pathEnv = $path.tostring() + "\env"
$pathRequirements = $path.tostring() + "\requirements.txt"
$pathDist = $path.tostring() + "\dist"

if (-not ((Test-Path $pathVenv -PathType Container) -or (Test-Path $pathEnv -PathType Container))){
    python -m venv venv
    if (-not (Test-Path -Path $pathRequirements -PathType leaf)){
        throw [System.IO.FileNotFoundException] "requirements.txt not found."
        exit
    }
}

venv\scripts\activate
pip install -r requirements.txt
pip install --upgrade build
python -m build
venv\scripts\deactivate

$dist = Get-ChildItem -Path $pathDist -Include "*.whl" -Recurse -Force -ErrorAction SilentlyContinue
$fileNameLib = $dist -split "\\"
$fileNameLib = $fileNameLib[-1]

$newPath = Read-Host 'Please enter the path where to transfer the library ( C:\dir )'

if (-not (Test-Path $newPath -PathType Container)){
    throw [System.IO.FileNotFoundException] "The entered directory does not exist or the path to it is entered incorrectly"
    exit
}

$newPathLib = $newPath + "\" + $fileNameLib

Move-Item -Path $dist -Destination $newPathLib

Remove-Item $pathDist -Force -Recurse

$ans = Read-Host "Do you want to install in a virtual environment ? (y/n)"

while (1) {
    if ($ans -eq "y"){
        $ans = Read-Host "Enter the name of your virtual environment"
        $pathNewVenv = $newPath + "\" + $ans
        if (-not (Test-Path $pathVenv -PathType Container)){
            throw [System.IO.FileNotFoundException] "The specified virtual environment does not exist or the path to it is incorrect"
            exit
        }
        $ActivatePath = $pathNewVenv + "\scripts\activate"
        Invoke-Expression $ActivatePath
        pip install $newPathLib
        Remove-Item $newPathLib
        $ActivatePath = $pathNewVenv + "\scripts\deactivate"
        Write-Host "Assembly and installation completed! Good luck with development"
        break
    }
    elseif ($ans -eq "n"){
        break
        Write-Host "Assembly completed! Good luck with development"
    }
    else {
        $ans = Read-Host "Do you want to install in a virtual environment ? (1/0)"
    }
}
