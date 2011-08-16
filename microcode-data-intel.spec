Summary:	Microcode definitions for Intel processors
Name:		microcode-data-intel
Version:	20110428
Release:	1
License:	INTEL SOFTWARE LICENSE AGREEMENT
Group:		Base
# http://downloadcenter.intel.com/, enter "microcode" to the search
Source0:	http://downloadmirror.intel.com/20050/eng/microcode-%{version}.tgz
# Source0-md5:	75b7d880f3a4b0161445a0dbdfe9c238
Provides:	microcode-data
ExclusiveArch:	i686 pentium2 pentium3 pentium4 %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
The microcode data file for Linux contains the latest microcode
definitions for all Intel processors.

%prep
%setup -q -c

%build
if ! grep -q 0x00000000 microcode.dat; then
	echo >&2 microcode.dat contains giberrish
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -a microcode.dat $RPM_BUILD_ROOT/lib/firmware/microcode.dat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) /lib/firmware/microcode.dat
