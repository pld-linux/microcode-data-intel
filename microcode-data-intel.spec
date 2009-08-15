Summary:	Microcode definitions for Intel processors
Name:		microcode-data-intel
Version:	20090330
Release:	1
License:	INTEL SOFTWARE LICENSE AGREEMENT
Group:		Base
# http://downloadcenter.intel.com/, enter "microcode" to the search
Source0:	http://downloadmirror.intel.com/14303/eng/microcode-%{version}.tgz
# Source0-md5:	5efec742621f830bd49ae11274766208
Provides:	microcode-data
ExclusiveArch:	i686 pentium2 pentium3 pentium4 x86_64 ia32e
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The microcode data file for Linux contains the latest microcode
definitions for all Intel processors.

%prep
%setup -q -c

%build
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install microcode*.dat $RPM_BUILD_ROOT/lib/firmware/microcode.dat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) /lib/firmware/microcode.dat
