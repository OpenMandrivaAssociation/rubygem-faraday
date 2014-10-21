%define oname faraday

Name:       rubygem-%{oname}
Version:    0.9.0
Release:    1
Summary:    HTTP/REST API client library
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/technoweenie/faraday
Source0:    http://rubygems.org/gems/faraday-0.9.0.gem
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
HTTP/REST API client library with pluggable components


%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore

%clean

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.document
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
# %doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
# %doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
# %doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
