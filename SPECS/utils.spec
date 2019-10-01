# Copyright 2019 Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%define COMPONENT utils
%define RPM_NAME caas-%{COMPONENT}
%define RPM_MAJOR_VERSION 1.0.0
%define RPM_MINOR_VERSION 8

Name:           %{RPM_NAME}
Version:        %{RPM_MAJOR_VERSION}
Release:        %{RPM_MINOR_VERSION}%{?dist}
Summary:        Containers as a Service supplementary utils
License:        %{_platform_license}
BuildArch:      noarch
Vendor:         %{_platform_vendor}
Source0:        %{name}-%{version}.tar.gz

Requires: initscripts

%description
This rpm contains the supplementary utils for caas subsystem.

%prep

%autosetup

%build

%install
mkdir -p %{buildroot}/%{_caas_libexec_path}/
# --------------------------- DEPLOY
install -m 0700 utils/deploy/merge_image.sh %{buildroot}/%{_caas_libexec_path}/
mkdir -p %{buildroot}/etc/systemd/system/
# --------------------------- COMMON
mkdir -p %{buildroot}/etc/profile.d/

%files
%{_caas_libexec_path}/merge_image.sh
%exclude %{_caas_libexec_path}/*pyc
%exclude %{_caas_libexec_path}/*pyo

%preun

%post
# --------------------------- DEPLOY
find /usr/lib/debug/usr/ -xtype l -exec rm -f {} \;

%postun


%clean
rm -rf ${buildroot}
