[Setup]
AppName=경찰청 인트라넷
AppVersion=1.0
DefaultDirName={pf}\경찰청 인트라넷
DefaultGroupName=경찰청 인트라넷
UninstallDisplayIcon={app}\경찰청 인트라넷.exe
OutputDir=.
OutputBaseFilename=경찰청_인트라넷_설치파일
SetupIconFile=police_logo.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "korean"; MessagesFile: "compiler:Languages\Korean.isl"

[Files]
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\경찰청 인트라넷"; Filename: "{app}\app.exe"; WorkingDir: "{app}"
Name: "{group}\Uninstall 경철청 인트라넷"; Filename: "{uninstallexe}"
Name: "{commondesktop}\경찰청 인트라넷"; Filename: "{app}\app.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "바탕화면에 바로가기 생성"; GroupDescription: "추가 아이콘:"
