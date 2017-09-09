Summary:	Microcode definitions for Intel processors
Summary(pl.UTF-8):	Definicje mikrokodu dla procesorów Intela
Name:		microcode-data-intel
Version:	20170707
Release:	2
License:	INTEL SOFTWARE LICENSE AGREEMENT
Group:		Base
# http://downloadcenter.intel.com/, enter "processor microcode data file" to the search
Source0:	http://downloadmirror.intel.com/26925/eng/microcode-%{version}.tgz
# Source0-md5:	fe4bcb12e4600629a81fb65208c34248
# Tool for splitting Intel's microcode file. From Fedora
Source1:	intel-microcode2ucode.c
# Produces single file for use by boot loader (like grub)
Source2:	intel-microcode2ucode-single.c
BuildRequires:	cpio
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
%setup -qc

%build
if ! grep -q 0x00000000 microcode.dat; then
	echo >&2 microcode.dat contains giberrish
	exit 1
fi

%{__cc} %{rpmcflags} %{rpmcppflags} %{rpmldflags} -Wall -o intel-microcode2ucode %{SOURCE1}
%{__cc} %{rpmcflags} %{rpmcppflags} %{rpmldflags} -Wall -o intel-microcode2ucode-single %{SOURCE2}
./intel-microcode2ucode microcode.dat > /dev/null || exit 1
./intel-microcode2ucode-single microcode.dat > /dev/null || exit 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib/firmware,/boot}

mv intel-ucode $RPM_BUILD_ROOT/lib/firmware

install -d kernel/x86/microcode
mv microcode.bin kernel/x86/microcode/GenuineIntel.bin
echo kernel/x86/microcode/GenuineIntel.bin | cpio -o -H newc -R 0:0 > $RPM_BUILD_ROOT/boot/intel-ucode.img

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/intel-ucode

%files initrd
%defattr(644,root,root,755)
/boot/intel-ucode.img
