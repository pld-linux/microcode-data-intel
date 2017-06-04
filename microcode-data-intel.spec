Summary:	Microcode definitions for Intel processors
Summary(pl.UTF-8):	Definicje mikrokodu dla procesorów Intela
Name:		microcode-data-intel
Version:	20170511
Release:	1
License:	INTEL SOFTWARE LICENSE AGREEMENT
Group:		Base
# http://downloadcenter.intel.com/, enter "processor microcode data file" to the search
Source0:	http://downloadmirror.intel.com/26798/eng/microcode-%{version}.tgz
# Source0-md5:	167e6e1ff234567291f067f48e11d740
# Tool for splitting Intel's microcode file. From Fedora
Source1:	intel-microcode2ucode.c
Provides:	microcode-data
ExclusiveArch:	i686 pentium2 pentium3 pentium4 %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The microcode data file for Linux contains the latest microcode
definitions for all Intel processors.

%description -l pl.UTF-8
Te pliki danych mikrokodu dla Linuksa zawierają najnowsze definicje
mikrokodu dla procesorów Intela.

%prep
%setup -q -c

%build
if ! grep -q 0x00000000 microcode.dat; then
	echo >&2 microcode.dat contains giberrish
	exit 1
fi

%{__cc} %{rpmcflags} %{rpmcppflags} %{rpmldflags} -Wall -o intel-microcode2ucode %{SOURCE1}
./intel-microcode2ucode microcode.dat > /dev/null || exit 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/lib/firmware}

install intel-microcode2ucode $RPM_BUILD_ROOT%{_sbindir}
mv intel-ucode $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/intel-microcode2ucode
/lib/firmware/intel-ucode
