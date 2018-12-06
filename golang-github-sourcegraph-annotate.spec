# Run tests in check section
%bcond_without check

%global goipath         github.com/sourcegraph/annotate
%global commit          f4cad6c6324d3f584e1743d8b3e0e017a5f3a636

%global common_description %{expand:
Apply multiple sets of annotations to a region of text.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Apply multiple sets of annotations to a region of text
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf4cad6c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418gitf4cad6c
- First package for Fedora

