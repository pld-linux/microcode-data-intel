Summary:	Microcode definitions for Intel processors
Summary(pl.UTF-8):	Definicje mikrokodu dla procesorów Intela
Name:		microcode-data-intel
Version:	20250812
Release:	1
License:	INTEL SOFTWARE LICENSE AGREEMENT
Group:		Base
Source0:	https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/archive/microcode-%{version}.tar.gz
# Source0-md5:	28bdd4dd8b21bfaa3b117875c44c4792
BuildRequires:	iucode-tool
Provides:	microcode-data
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The microcode data file for Linux contains the latest microcode
definitions for all Intel processors.

%description -l pl.UTF-8
Te pliki danych mikrokodu dla Linuksa zawierają najnowsze definicje
mikrokodu dla procesorów Intela.

%package initrd
Summary:	Microcode for initrd
Summary(pl.UTF-8):	Mikrokod dla initrd
Group:		Base

%description initrd
Intel microcode for initrd.

%description initrd -l pl.UTF-8
Mikrokod dla procesorów Intel dla initrd.

%prep
%setup -q -n Intel-Linux-Processor-Microcode-Data-Files-microcode-%{version}

%build
%{_sbindir}/iucode_tool intel-ucode*/*-* -tb --write-to=microcode.bin

install -d kernel/x86/microcode
ln microcode.bin kernel/x86/microcode/GenuineIntel.bin
echo kernel/x86/microcode/GenuineIntel.bin | cpio -o -H newc -R 0:0 > intel-ucode.img

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib/firmware,/boot}

cp -a intel-ucode $RPM_BUILD_ROOT/lib/firmware
cp -p intel-ucode.img $RPM_BUILD_ROOT/boot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md releasenote.md security.md
/lib/firmware/intel-ucode

%files initrd
%defattr(644,root,root,755)
%doc README.md releasenote.md security.md
/boot/intel-ucode.img
