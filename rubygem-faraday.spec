%define rbname faraday

Summary:	HTTP/REST API client library
Name:		rubygem-%{rbname}
Version:	0.9.0
Release:	1
License:	MIT
Group:		Development/Ruby
Url:		http://rubygems.org/gems/%{rbname}
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
HTTP/REST API client library with pluggable components

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
Conflicts:	%{name} < 0.9.0

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install
