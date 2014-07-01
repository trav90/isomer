Name: palemoon
Version: __PM_VERSION__
Release: 1%{?dist}
Summary: Firefox based web browser
Group: Development/Tools
License: MPLv2
URL: http://www.palemoon.org/
Source0: palemoon-__PM_VERSION__.tar
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%description
Pale Moon is a Firefox based web browser designed for efficiency that comes with an UI similar to what was present in older versions of Firefox.

%prep
%setup -q

%build

%install
cp -r * $RPM_BUILD_ROOT/

%clean
rm -rf $RPM_BUILD_ROOT

%post
gtk-update-icon-cache -f /usr/share/icons/hicolor
update-desktop-database -q

%postun
gtk-update-icon-cache -f /usr/share/icons/hicolor
update-desktop-database -q

%files
