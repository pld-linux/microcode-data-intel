Summary:	Microcode definitions for Intel processors
Summary(pl.UTF-8):	Definicje mikrokodu dla procesorów Intela
Name:		microcode-data-intel
Version:	20180425
Release:	1
License:	INTEL SOFTWARE LICENSE AGREEMENT
Group:		Base
# http://downloadcenter.intel.com/, enter "processor microcode data file" to the search
Source0:	https://downloadmirror.intel.com/27591/eng/microcode-%{version}.tgz
# Source0-md5:	99c80f9229554953a868127cda44e7e3
Provides:	microcode-data
BuildRequires:	iucode-tool
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
%setup -qc

%build

%{_sbindir}/iucode_tool intel-ucode*/*-* --write-to=microcode.bin

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
%doc releasenote
/lib/firmware/intel-ucode

%files initrd
%doc releasenote
%defattr(644,root,root,755)
/boot/intel-ucode.img
