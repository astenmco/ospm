FROM {{ from_image }}

#[AUTOLABEL_PROJECT_BEGIN]
LABEL project-name="{{ project_name }}"
LABEL project-full-name="{{ project_full_name }}"
LABEL project-author="{{ project_author }}"
LABEL project_description="{{ project_description }}" 
LABEL project_description="{{ project_customer }}" 
LABEL project_description="{{ project_contract_ref }}" 
LABEL project-repo="project_repo "
#[AUTOLABEL_PROJECT_END]

#[AUTOLABEL_DEPLOY_BEGIN]
LABEL branch="{{ {{ branch }} }}"
LABEL commit="{{ {{ commit }} }}"
#[AUTOLABEL_DEPLOY_END]

